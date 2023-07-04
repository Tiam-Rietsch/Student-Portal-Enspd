from django.db import models

class Cycle(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Level(models.Model):
    name = models.CharField(max_length=200)
    cycle = models.ForeignKey(Cycle, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return f'{self.name} - {self.cycle}'



class Field(models.Model):
    GEN_COURSE = 'Gen_Course'
    ELEC_E = 'Eelec_E'
    COMP_E = 'Comp_E'
    PROC_E = 'Proc_E'
    CIVIL_E = 'Civil_E'
    MECHA_E = 'Mecha_E'

    FIELD_CHOICE = [
        (GEN_COURSE, 'General Course'),
        (ELEC_E, 'Electrical Engineering'),
        (COMP_E, 'Computer Engineering'),
        (PROC_E, 'Process Engineering'),
        (CIVIL_E, 'Civil Engineering'),
        (MECHA_E, 'Mechanical Engineering')
    ]

    field_name = models.CharField(max_length=10, choices=FIELD_CHOICE, default=GEN_COURSE, null=True, blank=True)
    levels = models.ManyToManyField(Level)

    def __str__(self):
        return self.get_field_name_display()
    

class ClassGroup(models.Model):
    name = models.CharField(max_length=100)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['level', 'name']

    def __str__(self):
        return f'{self.level.cycle} {self.level.name} - {self.name} '