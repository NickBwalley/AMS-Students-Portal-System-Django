# Generated by Django 3.2 on 2021-05-21 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0018_remove_user_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default_profile_pic.jpg', null=True, upload_to=''),
        ),
    ]