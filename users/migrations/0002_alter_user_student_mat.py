# Generated by Django 4.2 on 2023-06-08 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='student_mat',
            field=models.CharField(max_length=8, unique=True),
        ),
    ]
