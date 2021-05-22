# Generated by Django 3.2 on 2021-05-21 05:51

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0011_user_profile_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed!')])),
                ('surname', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed!')])),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('phonenumber', models.CharField(max_length=30, unique=True, validators=[django.core.validators.RegexValidator('^[0-9]{10,12}$', 'Only Numerical characters are allowed! (Must be 10-12Digits)')])),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='App1.country')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='App1.course')),
                ('university', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='App1.university')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]