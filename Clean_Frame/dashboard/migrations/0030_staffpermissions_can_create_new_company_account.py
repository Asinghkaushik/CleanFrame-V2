# Generated by Django 2.2.19 on 2021-03-22 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0029_staffpermissions_can_unban_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffpermissions',
            name='can_create_new_company_account',
            field=models.BooleanField(default=False),
        ),
    ]
