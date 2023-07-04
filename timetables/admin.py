from django.contrib import admin

from .models import ClassTimeTable, Subject, ClassTimeSlot

class ClassTimeSlotInline(admin.TabularInline):
    model = ClassTimeSlot
    extra = 0



class ClassTimeTableAdmin(admin.ModelAdmin):
    inlines = [
        ClassTimeSlotInline
    ]


class SubjectAdmin(admin.ModelAdmin):
    inlines = [
        ClassTimeSlotInline
    ]



admin.site.register(ClassTimeTable, ClassTimeTableAdmin)
admin.site.register(ClassTimeSlot)
admin.site.register(Subject, SubjectAdmin)