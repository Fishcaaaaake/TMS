# Generated by Django 4.0.4 on 2022-05-30 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_usernames_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance_info',
            name='in_time',
            field=models.DateTimeField(),
        ),
    ]
