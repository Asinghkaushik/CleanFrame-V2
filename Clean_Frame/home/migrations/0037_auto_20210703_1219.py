# Generated by Django 3.1.13 on 2021-07-03 06:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0036_auto_20210702_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyprofile',
            name='code_expired',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='code_expired',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='otp_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 3, 12, 19, 46, 25227)),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='profile_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 3, 12, 19, 46, 25227)),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='signup_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 3, 12, 19, 46, 25227)),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='unique_code_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 3, 12, 19, 46, 29259)),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='otp_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 3, 12, 19, 46, 25227)),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='profile_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 3, 12, 19, 46, 25227)),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='signup_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 3, 12, 19, 46, 25227)),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='unique_code_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 3, 12, 19, 46, 25227)),
        ),
    ]
