from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from . forms import CreateUserForm

def register(request):
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()

	context = {'form':form}
	return render(request, 'App1/register.html', context)


def login(request):
	context = {}
	return render(request, 'App1/login.html')
