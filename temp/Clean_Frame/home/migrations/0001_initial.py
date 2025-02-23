# Generated by Django 3.1.5 on 2021-01-31 19:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_number', models.IntegerField(null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='post_images/')),
                ('cv', models.FileField(blank=True, null=True, upload_to='post_files/')),
                ('complete_address', models.CharField(max_length=1000, null=True)),
                ('gender', models.CharField(max_length=100, null=True)),
                ('profile_created', models.DateTimeField(auto_now=True)),
                ('account_banned_permanent', models.BooleanField(default=False)),
                ('account_banned_temporary', models.BooleanField(default=False)),
                ('account_ban_date', models.DateTimeField(blank=True, null=True)),
                ('account_ban_time', models.IntegerField(default=0)),
                ('signup_date', models.DateTimeField(auto_now=True)),
                ('verified', models.BooleanField(default=False)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
