from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from . models import user, MyAccountManager


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class create_user_form(UserCreationForm):
	class Meta:
		model = user
		fields = ['firstname', 'surname', 'email', 'phonenumber', 'country', 'university', 'course']
