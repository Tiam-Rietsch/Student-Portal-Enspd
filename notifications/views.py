from django.shortcuts import render, redirect
from users.models import User
from levels.models import Field, Cycle

from .models import Notification

# Create your views here.
def create_notification_view(request):

    if request.method == 'POST':
        matricules = request.POST.getlist('selected-mat')
        message = request.POST.get('notice-message')
        if message != '':
            for mat in matricules:
                receiver = User.objects.get(user_mat=mat)

                Notification.objects.create(
                    receiver=receiver,
                    sender=request.user,
                    body=message
                ).save() 

            return redirect('dashboard')   

    users = User.objects.exclude(groups__name='Administration')
    fields = Field.objects.all()
    cycles = Cycle.objects.all()
    context = {
        'users': users,
        'fields': fields,
        'cycles': cycles,
    }

    return render(request, 'notifications/send_notification.html', context)



def received_notifications_view(request):
    notifications = request.user.received_notifications.all()
    context = {
        "notifications": notifications
    }
    return render(request, 'notifications/received_notifications.html', context)