import datetime as dt
import os
from django.conf import settings
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.db.models import Q
from django.contrib import messages
from django.http import JsonResponse

from .models import User, StudentProfile
from levels.models import Field, Cycle, Level
from timetables.models import ClassTimeTable, ClassTimeSlot

def login_view(request):

    if request.method == 'POST':
        user_mat = request.POST['matricule'].upper()
        password = request.POST['password']

        user = authenticate(request, user_mat=user_mat, password=password)


        if user is not None:
            login(request, user)
            return redirect('enspd_home')
        else:
            messages.add_message(request, messages.ERROR, 'ERROR: Invalid data!, Check Password or Matricule')
    
    return render(request, 'users/login.html')


def logout_view(request):
    logout(request)
    return redirect('index')



def signup_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_mat = request.POST['matricule']
        passowrd = request.POST['password']

        cycle = request.POST['cycle']
        level = request.POST['level']
        field = request.POST['field']

        # first check if this matricule already exists
        try:
            user = User.objects.get(user_mat=user_mat)
            return redirect('login')
        except User.DoesNotExist:
            user = None


        if user is None:
            # add the user to the database
            user = User.objects.create_user(
                first_name=first_name.capitalize(),
                last_name=last_name.capitalize(),
                user_mat=user_mat.upper(),
                password=passowrd,
                username=first_name
            )

            first_names = user.first_name.split()
            last_names = user.last_name.split()

            if len(first_names) > 1:
                user.username = first_names[0] + first_names[1]
            else:
                user.username = first_names[0] + last_names[0]

            user.username = user.username.lower()
            user.save()

            # add a profile to the user
            profile = StudentProfile.objects.create(user=user)
            profile.cycle = Cycle.objects.get(name=cycle.upper())
            profile.level = profile.cycle.level_set.get(name=level)
            profile.field = profile.level.field_set.get(field_name=[user_field.field_name for user_field in Field.objects.all() if user_field.get_field_name_display() == field][0])
            profile.save()


            # login the user
            login(request, user)
            return redirect('enspd_home')
        

    else:
        return render(request, 'users/signup.html', {'fields': Field.objects.all()})
    

def profile_page_view(request):
    time_tables = ClassTimeTable.objects.filter(
        cycle=request.user.student_profile.cycle, 
        level=request.user.student_profile.level, 
        field=request.user.student_profile.field,
    )

    time_tables = time_tables.filter(
        (Q(start_date=datetime.today()) | Q(start_date__lt=datetime.today())) &
        (Q(end_date=datetime.today()) | Q(end_date__gt=datetime.today()))
    )

    if time_tables.count() == 0:
        start = datetime.now() - dt.timedelta(days=datetime.now().weekday())
        end = start + dt.timedelta(days=6)
        class_time_table = ClassTimeTable.objects.create(
            name='Time Table',
            cycle=request.user.student_profile.cycle, 
            level=request.user.student_profile.level, 
            field=request.user.student_profile.field,
            start_date = start,
            end_date=end
        )
    else:
        class_time_table = time_tables[0]

    date = datetime.today()
    time_slots = ClassTimeSlot.objects.filter(Q(time_table=class_time_table) & Q(class_groups__in=[request.user.student_profile.class_group]))
    day_program = [slot for slot in time_slots if datetime.strftime(datetime.now(), "%a").upper() == slot.day.upper()]
    context = {
        'time_slots': time_slots,
        'table': class_time_table,
        'day_program': day_program,
        'current_date': f'{date.day}/{date.month}/{date.year}'
    }
    return render(request, 'users/profile.html', context)


def edit_profile_photos(request):
    if request.method == 'POST':
        cover_photo = request.FILES.get('cover-image')
        profile_picture = request.FILES.get('profile-picture')

        # use this in development for static files
        blank_profile_picture = '/static/img/blank-profile-picture.png'
        blank_cover_photo = '/static/img/blank-cover-photo.jpg'

        print(cover_photo)

        if cover_photo:
            if request.user.cover_photo.url != blank_cover_photo: 

                # in development when MEDIA_ROOT is set
                os.remove(os.path.join(settings.MEDIA_ROOT, request.user.cover_photo.name))

            request.user.cover_photo = cover_photo

        if profile_picture:
            if request.user.profile_photo.url != blank_profile_picture:

                # in development when MEDIA_ROOT is set
                os.remove(os.path.join(settings.MEDIA_ROOT, request.user.profile_photo.name))

            request.user.profile_photo = profile_picture


        request.user.save()

        return redirect('profile')
    else:
        return render(request, 'users/edit-profile-page.html')
 

def admin_dashboard_view(request):
    return render(request, 'users/admin_dashboard.html')


def get_slot_data(request):
    if request.headers['X-Requested-With'] == 'getSlotData':
        slot = ClassTimeSlot.objects.get(id=int(request.GET.get('pk'))) 
        return JsonResponse({
            'start_time': slot.start_time,
            'end_time': slot.end_time,
            'type': slot.slot_type,
        })


def get_calendar(request):
    date = request.GET.get('selDate')
    date = datetime.strptime(date, '%m/%d/%Y')

    time_tables = ClassTimeTable.objects.filter(
        cycle=request.user.student_profile.cycle, 
        level=request.user.student_profile.level, 
        field=request.user.student_profile.field,
    )

    time_tables = time_tables.filter(
        (Q(start_date=date) | Q(start_date__lt=date)) &
        (Q(end_date=date) | Q(end_date__gt=date))
    )

    if time_tables.count() == 0:
        start = date - dt.timedelta(days=date.weekday())
        end = start + dt.timedelta(days=6)
        class_time_table = ClassTimeTable.objects.create(
            cycle=request.user.student_profile.cycle, 
            level=request.user.student_profile.level, 
            field=request.user.student_profile.field,
            start_date = start,
            end_date=end
        )
    else:
        class_time_table = time_tables[0]


    time_slots = ClassTimeSlot.objects.filter(Q(time_table=class_time_table) & Q(class_groups__in=[request.user.student_profile.class_group]))
    day_program = [slot for slot in time_slots if datetime.strftime(datetime.now(), "%a").upper() == slot.day.upper()]
    context = {
        'time_slots': time_slots,
        'table': class_time_table,
        'day_program': day_program,
        'current_date': f'{date.day}/{date.month}/{date.year}'
    }
    return render(request, 'users/profile.html', context)
