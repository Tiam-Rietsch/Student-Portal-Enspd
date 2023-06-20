from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from .models import User
from levels.models import Field

def login_view(request):
    return render(request, 'users/login.html')


def signup_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_mat = request.POST['matricule']
        passowrd = request.POST['password']

        # first check if this matricule already exists
        try:
            user = User.objects.get(user_mat=user_mat)
            return redirect('login')
        except User.DoesNotExist:
            user = None

        # then create a user in the database
        if user is None:
            user = User.objects.create(
                first_name=first_name.capitalize(),
                last_name=last_name.capitalize(),
                user_mat=user_mat.upper(),
                password=passowrd
            )
            user.save()
            login(request, user)
            return redirect('home')
        

    else:
        return render(request, 'users/signup.html', {'fields': Field.objects.all()})