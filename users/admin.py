from django.contrib import admin
from .models import User, StudentProfile, AdminProfile

class StudentProfileInline(admin.TabularInline):
    model = StudentProfile
    extra = 0


class AdminProfileInline(admin.TabularInline):
    model = AdminProfile
    extra = 0


class StudentGroupInline(admin.TabularInline):
    model = StudentProfile.class_groups.through
    extra = 0


class StudentProfileAdmin(admin.ModelAdmin):
    inlines = [
        StudentGroupInline,
    ]


class UserAdmin(admin.ModelAdmin):
    inlines = [
        StudentProfileInline,
        AdminProfileInline,
    ]


admin.site.register(User, UserAdmin)
admin.site.register(StudentProfile, StudentProfileAdmin)
admin.site.register(AdminProfile)