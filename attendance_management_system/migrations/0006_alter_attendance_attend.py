# Generated by Django 4.0.1 on 2022-03-20 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_management_system', '0005_remove_attendance_attend_attendance_attend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='attend',
            field=models.CharField(default=1, max_length=40),
        ),
    ]
