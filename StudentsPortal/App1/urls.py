from django.urls import path
from . import views


urlpatterns = [
	path('register/', views.registration_page, name='register'),
	path('login/', views.login_page, name='login'),
	path('', views.home, name='home')
]