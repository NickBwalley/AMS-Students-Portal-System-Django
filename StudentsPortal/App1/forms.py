from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from django import forms
from App1.models import user, Country, University, Course


# class CreateUserForm(UserCreationForm):
# 	class Meta:
# 		model = User
# 		fields = ['username', 'email', 'password1', 'password2']

class create_user_form(UserCreationForm):
	class Meta:
		model = user
		fields = ['firstname', 'surname', 'email', 'phonenumber', 'country', 'university', 'course', 'profile_pic']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['university'].queryset = University.objects.none()
		self.fields['course'].queryset = Course.objects.none()

		if 'country' in self.data:
			try:
				country_id = int(self.data.get('country'))
				self.fields['university'].queryset =University.objects.filter(country_id=country_id).order_by('name')
			except (ValueError, TypeError):
				pass # invalid input from the client; ignore and fallback to empty University queryset
		elif self.instance.pk:
			self.fields['university'].queryset = self.instance.country.university_set.order_by('name')

		if 'university' in self.data:
			try:
				university_id = int(self.data.get('university'))
				self.fields['course'].queryset =Course.objects.filter(university_id=university_id).order_by('name')
			except (ValueError, TypeError):
				pass # invalid input from the client; ignore and fallback to empty University queryset
		elif self.instance.pk:
			self.fields['course'].queryset = self.instance.university.course_set.order_by('name')

	