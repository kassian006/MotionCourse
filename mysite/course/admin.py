from django.contrib import admin
from .models import *

class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1


class VideoCourseInline(admin.TabularInline):
    model = VideoCourse
    extra = 1


class MainCourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]


class LessonAdmin(admin.ModelAdmin):
    inlines = [VideoCourseInline]


admin.site.register(Lesson, LessonAdmin)
admin.site.register(MainCourse, MainCourseAdmin)
admin.site.register(Favorite)
admin.site.register(FavoriteItem)
admin.site.register(AboutUs)
admin.site.register(JoinUs)
admin.site.register(Category)
admin.site.register(CourseReview)
