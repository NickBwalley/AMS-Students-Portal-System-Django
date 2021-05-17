from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
from . forms import CreateUserForm, create_user_form
from .decorators import *

@unauthenticated_user
def registration_page(request):
	form = create_user_form()

	if request.method == 'POST':
		form = create_user_form(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('firstname') # allows to get only the username without any other details
			messages.success(request, 'Account successfully created for: ' + user)
			return redirect('login')

	context = {'form':form}
	return render(request, 'App1/register2.html', context)

@unauthenticated_user
def login_page(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Incorrect Username or Password!')

	context = {}
	return render(request, 'App1/login.html', context)


def logout_user(request):
	logout(request)
	return redirect('login')


@login_required(login_url='login') # only allows users who are logged in with correct credentials
def home(request):
	return render(request, 'App1/dashboard.html')