# Generated by Django 3.2 on 2021-05-21 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0022_auto_20210521_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
