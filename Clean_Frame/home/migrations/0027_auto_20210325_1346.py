# Generated by Django 2.2.19 on 2021-03-25 13:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_auto_20210325_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='otp_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 25, 13, 46, 35, 980930)),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='profile_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 25, 13, 46, 35, 980716)),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='signup_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 25, 13, 46, 35, 980843)),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='otp_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 25, 13, 46, 35, 979587)),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='profile_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 25, 13, 46, 35, 979502)),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='signup_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 25, 13, 46, 35, 979566)),
        ),
    ]
