from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


admin.site.register(MainCourse)
admin.site.register(Favorite)
admin.site.register(FavoriteItem)
admin.site.register(CourseReview)