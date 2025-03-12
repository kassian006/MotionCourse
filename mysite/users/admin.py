from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


admin.site.register(Country)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(City)
admin.site.register(UserProfile)
admin.site.register(Student)
admin.site.register(Owner)
admin.site.register(Group)
admin.site.register(GroupMember)
admin.site.register(Message)
