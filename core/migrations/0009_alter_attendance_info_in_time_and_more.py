# Generated by Django 4.0.4 on 2022-05-31 13:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_attendance_info_in_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance_info',
            name='in_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 31, 15, 55, 19, 328459)),
        ),
        migrations.AlterField(
            model_name='attendance_info',
            name='out_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
