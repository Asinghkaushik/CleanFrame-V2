# Generated by Django 2.2.19 on 2021-03-22 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0031_staffpermissions_can_manage_blogs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100000)),
                ('short_description', models.CharField(max_length=100000000)),
                ('brief_description', models.TextField()),
                ('file', models.FileField(blank=True, null=True, upload_to='post_files/')),
            ],
        ),
    ]
