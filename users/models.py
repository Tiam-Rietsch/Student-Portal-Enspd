from django.db import models
from django.contrib.auth.models import AbstractUser

from levels.models import Level, ClassGroup, Cycle, Field

class User(AbstractUser):
    user_mat = models.CharField(max_length=8, unique=True)

    USERNAME_FIELD = 'user_mat'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    def __str__(self):
        return self.username


class StudentProfile(models.Model):
    STUDENT = 'STD'
    DELEGATE = 'DEL'
    ENGINEER = 'ENG'
    SC_ENGINEER = 'SC_ENG'
    USERS_STATUSES = [
        (STUDENT, 'Student'),
        (DELEGATE, 'Delegate'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_status = models.CharField(max_length=3, choices=USERS_STATUSES, default=STUDENT, null=True, blank=True)

    cycle = models.ForeignKey(Cycle, on_delete=models.CASCADE, null=True, blank=True)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, null=True)
    field = models.ForeignKey(Field, on_delete=models.CASCADE, blank=True, null=True)
    class_groups = models.ManyToManyField(ClassGroup, null=True, blank=True)

    def __str__(self):
        return self.user.username


class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.username
    