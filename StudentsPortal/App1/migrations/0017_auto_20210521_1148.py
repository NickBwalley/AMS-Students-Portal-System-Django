# Generated by Django 3.2 on 2021-05-21 11:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0016_auto_20210521_0911'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_profile',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='last_login',
        ),
        migrations.AddField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='date joined'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(auto_now=True, default=django.utils.timezone.now, verbose_name='last login'),
            preserve_default=False,
        ),
    ]
