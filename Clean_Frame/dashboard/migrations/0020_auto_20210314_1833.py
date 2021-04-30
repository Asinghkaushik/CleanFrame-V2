# Generated by Django 2.2.19 on 2021-03-14 18:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0019_auto_20210313_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentregistration',
            name='date_of_registrations',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='ProfilePermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_who_can_see', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='can_see', to=settings.AUTH_USER_MODEL)),
                ('user_whose_to_see', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='whose_to_see', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
