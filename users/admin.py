from django.contrib import admin
from .models import User, StudentProfile, AdminProfile
from .forms import CreateUserForm, ChangeUserForm


class StudentProfileInline(admin.TabularInline):
    model = StudentProfile
    extra = 0


class AdminProfileInline(admin.TabularInline):
    model = AdminProfile
    extra = 0


class StudentInline(admin.TabularInline):
    model = StudentProfile
    extra = 0


class UserAdmin(admin.ModelAdmin):
    change_form = ChangeUserForm
    add_form = CreateUserForm
    inlines = [
        StudentProfileInline,
        AdminProfileInline,
    ]
    list_display = ['first_name', 'last_name', 'username', 'is_staff']
    model = User

    def get_form(self, request, obj=None, **kwargs):
        if not obj:
            self.form = self.add_form
        else:
            self.form = self.change_form

        return super(UserAdmin, self).get_form(request, obj, **kwargs)


admin.site.register(User, UserAdmin)
admin.site.register(StudentProfile)
admin.site.register(AdminProfile)