# Generated by Django 2.2.19 on 2021-03-22 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0030_staffpermissions_can_create_new_company_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffpermissions',
            name='can_manage_blogs',
            field=models.BooleanField(default=True),
        ),
    ]
