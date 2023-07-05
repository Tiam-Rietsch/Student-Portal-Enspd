from django.db import models
from users.models import User


# Create your models here.
class Notification(models.Model):
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_notifications')
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='sent_notifications')
    date_created = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    
    def __str__(self):
        return '@' + self.sender.username + ' to @' + self.receiver.username + ':  ' + self.body[:50]
    