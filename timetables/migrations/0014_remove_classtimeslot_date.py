# Generated by Django 4.2.1 on 2023-06-25 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetables', '0013_classtimeslot_date_classtimeslot_end_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classtimeslot',
            name='date',
        ),
    ]
