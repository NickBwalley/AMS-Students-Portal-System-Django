# Generated by Django 3.2 on 2021-05-27 17:50

import App1.models
import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0026_alter_profile_bio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='user',
            name='surname',
        ),
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.CharField(blank=True, default='Hey there...', max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='hide_email',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='hide_phonenumber',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, default=App1.models.get_default_profile_image, null=True, upload_to=App1.models.get_profile_image_filepath),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=django.utils.timezone.now, max_length=30, unique=True, validators=[django.core.validators.RegexValidator('^[A-Za-z0-9_.]*$', 'Only Letters, Numbers, Underscores and Periods are allowed!')]),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
