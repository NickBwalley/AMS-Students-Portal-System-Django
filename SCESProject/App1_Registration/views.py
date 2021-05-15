from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def registration(request):
	return render(request, "App1_Registration/register.html")


def login(request):
	return render(request, "App1_Registration/login.html")

