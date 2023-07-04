from django.db import models
from datetime import datetime as dt

from levels.models import Cycle, Level, Field, ClassGroup
# Create your models here.
class ClassTimeTable(models.Model):
    SEMESTERS = [
        ("S1", "SEMESTER 1"),
        ("S2", "SEMESTER 2"),
        ("S3", "SEMESTER 3"),
        ("S4", "SEMESTER 4"),
        ("S5", "SEMESTER 5"),
        ("S6", "SEMESTER 6"),
        ("S7", "SEMESTER 7"),
        ("S8", "SEMESTER 8"),
        ("S9", "SEMESTER 9"),
        ("S10", "SEMESTER 10"),
    ]

    name = models.CharField(max_length=100)
    semester = models.CharField(max_length=3, choices=SEMESTERS, default="S4", null=True, blank=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    cycle =  models.ForeignKey(Cycle, on_delete=models.CASCADE, default=True, null=True)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, default=True, null=True)
    field = models.ForeignKey(Field, on_delete=models.CASCADE, default=True, null=True)

    def __str__(self):
        start = f'{self.start_date.day}-{self.start_date.month}-{self.start_date.year}' 
        end = f'{self.end_date.day}-{self.end_date.month}-{self.end_date.year}'
        return  f'{self.level.name} from {start} to {end}: {self.field.get_field_name_display()} {self.semester} - {self.cycle.name}  '
    

class ClassTimeSlot(models.Model):
    DAY_CHOICES = [
        ('MON', 'MONDAY'),
        ('TUE', 'TUESDAY'),
        ('WED', 'WEDNESDAY'),
        ('THU', 'THURSDAY'),
        ('FRI', 'FRIDAY'),
        ('SAT', 'SATURDAY'),
        ('SUN', 'SUNDAY')
    ]

    TYPES = [
        ('TD', 'TD'),
        ('Exam', 'Exam'),
        ('Class', 'Class'),
        ('TP', 'TP'),
        ('CA', 'CA')
    ]

    day = models.CharField(max_length=3, choices=DAY_CHOICES, null=True, blank=True)
    slot_type = models.CharField(max_length=8, choices=TYPES, null=True, blank=True)

    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    
    time_table = models.ForeignKey(ClassTimeTable, on_delete=models.CASCADE, related_name='time_slots')
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    class_groups = models.ManyToManyField(ClassGroup, blank=True, null=True)


    class Meta:
        ordering = ['start_time']

    def __str__(self):
        return f'{self.subject} - start: {self.start_time} stop: {self.end_time}'



class Subject(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=15)

    def __str__(self):
        return self.name
