from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages
# Create your views here.
from . forms import CreateUserForm

def register(request):
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username') # allows to get only the username without any other details
			messages.success(request, 'Account successfully created for: ' + user)
			return redirect('login')

	context = {'form':form}
	return render(request, 'App1/register.html', context)


def login(request):
	context = {}
	return render(request, 'App1/login.html')
