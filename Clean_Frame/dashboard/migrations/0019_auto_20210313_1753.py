# Generated by Django 2.2.19 on 2021-03-13 17:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0018_auto_20210313_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentregistration',
            name='date_of_registrations',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 13, 17, 53, 13, 122186, tzinfo=utc)),
        ),
    ]
