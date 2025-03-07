from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


admin.site.register(Country)
admin.site.register(City)
admin.site.register(UserProfile)
admin.site.register(Student)
admin.site.register(Owner)
