# Generated by Django 3.1.6 on 2021-03-02 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20210302_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='image',
            field=models.ImageField(default='us_ma.png', upload_to='post_images/'),
        ),
    ]
