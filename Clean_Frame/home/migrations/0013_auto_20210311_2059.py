# Generated by Django 2.2.19 on 2021-03-11 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_studentprofile_cgpa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='cgpa',
            field=models.FloatField(default=0.0, null=True),
        ),
    ]
