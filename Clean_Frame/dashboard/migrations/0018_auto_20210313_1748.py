# Generated by Django 2.2.19 on 2021-03-13 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0017_auto_20210313_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentregistration',
            name='date_of_registrations',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
