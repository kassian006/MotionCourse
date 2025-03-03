from .views import *
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'main_course', MainCourseListViewSet, basename='main_course'),
router.register(r'favorite', FavoriteListViewSet, basename='favorite'),
router.register(r'favorite_item', FavoriteItemListViewSet, basename='favorite_item_'),
router.register(r'course_review', CourseReviewListViewSet, basename='course_review'),

urlpatterns = [
    path('', include(router.urls)),
]