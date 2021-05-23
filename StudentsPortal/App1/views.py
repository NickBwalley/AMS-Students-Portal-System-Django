from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
from .forms import *
from .models import *
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

@login_required(login_url='login') # only allows users who are logged in with correct credentials
def my_profile(request):
	user = request.user
	form = update_user_profile(instance=user)

	if request.method == 'POST':
		form = update_user_profile(request.POST, request.FILES,instance=user)
		if form.is_valid:
			form.save()
			
	context = {'form':form}
	return render(request, 'App1/my_profile.html', context)

# AJAX
def load_cities(request):
    country_id = request.GET.get('country_id')
    universities = University.objects.filter(country_id=country_id).all()
    return render(request, 'App1/university_dropdown_list_options.html', {'universities': universities})

def load_cities2(request):
    university_id = request.GET.get('university_id')
    courses = Course.objects.filter(university_id=university_id).all()
    return render(request, 'App1/course_dropdown_list_options.html', {'courses': courses})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)
    


