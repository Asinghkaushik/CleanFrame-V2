# Generated by Django 2.2.19 on 2021-03-25 01:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20210325_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='otp_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 25, 1, 53, 46, 917435)),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='profile_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 25, 1, 53, 46, 917357)),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='signup_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 25, 1, 53, 46, 917414)),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='otp_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 25, 1, 53, 46, 916464)),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='profile_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 25, 1, 53, 46, 916382)),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='signup_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 25, 1, 53, 46, 916443)),
        ),
    ]
