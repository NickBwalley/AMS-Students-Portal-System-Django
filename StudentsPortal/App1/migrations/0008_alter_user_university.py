# Generated by Django 3.2 on 2021-05-18 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0007_auto_20210518_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='university',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='App1.university'),
        ),
    ]