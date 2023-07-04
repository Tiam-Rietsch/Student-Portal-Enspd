from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['is_staff', 'first_name', 'last_name', 'user_mat', 'username', 'groups']


class ChangeUserForm(UserChangeForm):

    class Meta:
        model = User
        fields = ['username', 'groups']