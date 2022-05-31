# Generated by Django 4.0.4 on 2022-05-31 13:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_attendance_info_delete_attendance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance_info',
            name='in_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 31, 15, 48, 28, 876136)),
        ),
        migrations.AlterField(
            model_name='attendance_info',
            name='out_time',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='attendance_info',
            name='total_duration',
            field=models.IntegerField(blank=True),
        ),
    ]
