from django.contrib import admin

from .models import Cycle, Level, Field, ClassGroup
from users.admin import StudentProfileInline, StudentGroupInline

class LevelInline(admin.TabularInline):
    model = Level
    extra = 0

class FieldLevelInline(admin.TabularInline):
    model = Field.levels.through
    extra = 0


class ClassGroupInline(admin.TabularInline):
    model = ClassGroup
    extra = 0


class CycleAdmin(admin.ModelAdmin):
    inlines = [
        LevelInline,
        StudentProfileInline
    ]


class LevelAdmin(admin.ModelAdmin):
    inlines = [
        FieldLevelInline,
        ClassGroupInline,
        StudentProfileInline,
    ]
    exclude = ['levels']


class FieldAdmin(admin.ModelAdmin):
    inlines = [
        FieldLevelInline,
        StudentProfileInline,
    ]


class ClassGroupAdmin(admin.ModelAdmin):
    inlines = [
        StudentGroupInline,
    ]
    exclude = ['class_groups']


# Register your models here.
admin.site.register(Cycle, CycleAdmin)
admin.site.register(Level, LevelAdmin)
admin.site.register(Field, FieldAdmin)
admin.site.register(ClassGroup, ClassGroupAdmin)

