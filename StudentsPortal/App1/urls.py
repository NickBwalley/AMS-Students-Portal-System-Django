from django.urls import path
from . import views


urlpatterns = [
	path('register/', views.registration_page, name='register'),
	path('login/', views.login_page, name='login'),
	path('logout/', views.logout_user, name='logout'),
	path('', views.home, name='home'),

	path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'), # AJAX
]