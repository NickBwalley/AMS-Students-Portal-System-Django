from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class University(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Course(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


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

	alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed!')
	# Regex to match 10 to 12 digits only
	phonenumber = RegexValidator(r'^[0-9]{10,12}$', 'Only Numerical characters are allowed! (Must be 10-12Digits)')

	firstname		= models.CharField(max_length=30, unique=False, validators=[alphanumeric])
	surname 		= models.CharField(max_length=30, unique=False, validators=[alphanumeric])
	email 			= models.EmailField(verbose_name="email", max_length=60, unique=True)
	phonenumber 	= models.CharField(max_length=30, unique=True, validators=[phonenumber])
	country 		= models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
	university 		= models.ForeignKey(University, on_delete=models.SET_NULL, null=True)
	course			= models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True, null=True)
	date_joined 	= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login		= models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin 		= models.BooleanField(default=False)
	is_active 		= models.BooleanField(default=True)
	is_staff 		= models.BooleanField(default=False)
	is_superuser 	= models.BooleanField(default=False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []
	
	objects = MyAccountManager()

	def __str__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return True

class Profile(models.Model):
	user 			= models.OneToOneField(user, on_delete=models.CASCADE)
	profile_pic 	= models.ImageField(null=True, default="default_profile_pic.jpg", upload_to="profile_pics")
	bio 			= models.CharField(max_length=150, null=True, blank=True)

	def __str__(self):
		return self.user.email