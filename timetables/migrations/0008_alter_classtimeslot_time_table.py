# Generated by Django 4.2.1 on 2023-06-25 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timetables', '0007_classtimetable_end_date_classtimetable_start_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classtimeslot',
            name='time_table',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='time_slots', to='timetables.classtimetable'),
        ),
    ]