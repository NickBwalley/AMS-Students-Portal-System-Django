from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.conf import settings

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
			user = form.cleaned_data.get('username') # allows to get only the username without any other details
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



@login_required(login_url='login') # only allows users who are logged in with correct credentials
def my_profile(request):
	user = request.user
	user_id = request.user.id
	form = update_user_profile(instance=user)

	if request.method == 'POST':
		form = update_user_profile(request.POST, request.FILES,instance=user)
		if form.is_valid:
			form.save()
			return redirect('my_profile')
			
			
	context = {'form':form}
	return render(request, 'App1/my_profile.html', context)


def other_profile(request):
	# context = {}
	
	return render(request, 'App1/other_profile.html')


@login_required(login_url='login') # only allows users who are logged in with correct credentials
def account_view(request, id):
	'''
	-LOGIC here is kind of tricky
		is_self(boolean)
			is_friend(boolean)
				-1: NO_REQUEST_SENT
				0: THEM_SENT_TO_YOU
				1: YOU_SENT_TO_THEM
	'''
	context = {}
	
	account = get_object_or_404(user, pk=id)
	
	# context = {}
	# user_id = kwargs.get("user_id")

	# try:
	# 	account = user.objects.get(pk=user_id)
	# except user.DoesNotExist:
	# 	return HttpResponse("That User doesn't Exist!")
	if account:
		context['id']: account.id
		context['username']: account.username
		context['email']: account.email
		context['profile_image']: account.profile_image.url
		context['hide_email']: account.hide_email
		context['hide_phonenumber']: account.hide_phonenumber

		# define state template variables
		is_self = False
		# is_friend = False

		user_id = request.user.id
		print(user_id)
		print(account.id)
		if user_id == account.id:
			is_self = True

		# context['user_id'] = user_id
		# context['is_self'] = is_self
		# context['is_friend'] = is_friend
		# context['BASE_URL'] = settings.BASE_URL
		# context = {'user_id': user_id, 'account_id': account.id}

	return render(request, "App1/other_profile.html", {'id':id, 'account':account, 'context': context})



def account_search_view(request, *args, **kwargs):
	context = {}

	if request.method == "GET":
		search_query = request.GET.get("q")
		if len(search_query) > 0:
			search_results = user.objects.filter(email__icontains=search_query).filter(username__icontains=search_query).distinct()
			# user = request.user
			accounts = []
			for account in search_results:
				accounts.append((account, False)) # You have no friends 
			context['accounts'] = accounts
	return render(request, "App1/search_results.html", context)




    


