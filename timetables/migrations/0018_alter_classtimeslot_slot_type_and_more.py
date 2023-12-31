# Generated by Django 4.2.1 on 2023-07-03 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetables', '0017_alter_classtimeslot_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classtimeslot',
            name='slot_type',
            field=models.CharField(blank=True, choices=[('TD', 'TD'), ('Exam', 'Exam'), ('Class', 'Class'), ('TP', 'TP'), ('CA', 'CA')], max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='classtimetable',
            name='semester',
            field=models.CharField(blank=True, choices=[('S1', 'SEMESTER 1'), ('S2', 'SEMESTER 2'), ('S3', 'SEMESTER 3'), ('S4', 'SEMESTER 4'), ('S5', 'SEMESTER 5'), ('S6', 'SEMESTER 6'), ('S7', 'SEMESTER 7'), ('S8', 'SEMESTER 8'), ('S9', 'SEMESTER 9'), ('S10', 'SEMESTER 10')], default='S4', max_length=3, null=True),
        ),
    ]
