from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from App1.models import *



class UserAdmin(UserAdmin):
	list_display = ('username', 'email', 'phonenumber', 'date_joined', 'is_admin', 'is_staff', 'is_verified')
	search_fields = ('email', 'username')
	readonly_fields = ('id',  'country', 'university', 'course',  'date_joined', 'last_login',)

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

admin.site.register(user, UserAdmin)

admin.site.register(Country)
admin.site.register(University)
admin.site.register(Course)


# class UniversityAdmin(UserAdmin):
# 	list_display = ('university', 'country')
# 	search_fields = ('university')
	
# 	filter_horizontal = ()
# 	list_filter = ()
# 	fieldsets = ()

# admin.site.register(University, UniversityAdmin)


# class CourseAdmin(UserAdmin):
# 	list_display = ('course', 'university', 'country')
# 	search_fields = ('course')
	
# 	filter_horizontal = ()
# 	list_filter = ()
# 	fieldsets = ()

# admin.site.register(Course, CourseAdmin)