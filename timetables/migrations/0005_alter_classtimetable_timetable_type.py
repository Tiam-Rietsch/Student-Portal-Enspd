# Generated by Django 4.2.1 on 2023-06-24 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetables', '0004_classtimetable_timetable_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classtimetable',
            name='timetable_type',
            field=models.CharField(blank=True, choices=[('TD', 'TD'), ('Exam', 'Exam'), ('Class', 'Class')], max_length=5, null=True),
        ),
    ]