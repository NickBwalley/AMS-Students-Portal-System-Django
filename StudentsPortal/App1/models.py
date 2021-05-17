from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator

# Create your models here.



class MyAccountManager(BaseUserManager):
	def create_user(self, email, password=None):
		if not email:
			raise ValueError("Student must have an Email")
		
		user = self.model(
			email = self.normalize_email(email),
			
		)

		user.set_password(password)
		user.save(using=self._db)
		return user


	def create_superuser(self, email, password):
		user = self.create_user(
			email = self.normalize_email(email),
			password = password,		
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user	


class user(AbstractBaseUser):

	alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
	phonenumber = RegexValidator(r'^[0-9]*$', 'Only Numerical characters are allowed.')

	firstname		= models.CharField(max_length=30, unique=False, validators=[alphanumeric])
	surname 		= models.CharField(max_length=30, unique=False, validators=[alphanumeric])
	email 			= models.EmailField(verbose_name="email", max_length=60, unique=True)
	phonenumber 	= models.CharField(max_length=30, unique=True, validators=[phonenumber])
	country 	= models.CharField(max_length=30, unique=False)
	university 		= models.CharField(max_length=60, unique=False)
	course			= models.CharField(max_length=60, unique=False)
	date_joined 	= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login		= models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin 		= models.BooleanField(default=False)
	is_active 		= models.BooleanField(default=True)
	is_staff 		= models.BooleanField(default=False)
	is_superuser 	= models.BooleanField(default=False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []
	
	objects = MyAccountManager()

	# def __str__(self):
	# 	return self.firstname 

	# def __str__(self):
	# 	return self.surname

	def __str__(self):
		return self.email

	# def __str__(self):
	# 	return self.phonenumber

	# def __str__(self):
	# 	return self.university

	# def __str__(self):
	# 	return self.course

	# def __str__(self):
	# 	return self.date_joined


	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return True

