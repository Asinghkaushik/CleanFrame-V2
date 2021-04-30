# Generated by Django 3.1.5 on 2021-02-01 14:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0004_auto_20210201_1320'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_number', models.IntegerField(null=True)),
                ('complete_address', models.CharField(max_length=1000, null=True)),
                ('profile_created', models.DateTimeField(auto_now=True)),
                ('account_banned_permanent', models.BooleanField(default=False)),
                ('account_banned_temporary', models.BooleanField(default=False)),
                ('account_ban_date', models.DateTimeField(blank=True, null=True)),
                ('account_ban_time', models.IntegerField(default=0)),
                ('signup_date', models.DateTimeField(auto_now=True)),
                ('verified', models.BooleanField(default=False)),
                ('otp_time', models.DateTimeField(auto_now=True)),
                ('otp', models.CharField(max_length=100, null=True)),
                ('stipend', models.FloatField(default=0, null=True)),
                ('internship_duration', models.IntegerField(default=0, null=True)),
                ('students_required', models.IntegerField(default=0, null=True)),
                ('internship_position', models.CharField(max_length=100, null=True)),
                ('minimum_cgpa', models.FloatField(default=5.0, null=True)),
                ('prerequisite', models.CharField(max_length=100, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
