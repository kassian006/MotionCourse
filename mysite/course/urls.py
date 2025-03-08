from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet,
    MainCourseListViewSet,
    LessonViewSet,
    AboutUsViewSet,
    JoinUsViewSet,
    FavoriteViewSet,
    FavoriteItemViewSet,
    CourseReviewViewSet
)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'main-courses', MainCourseListViewSet, basename='maincourse')
router.register(r'lessons', LessonViewSet, basename='lesson')
router.register(r'about-us', AboutUsViewSet, basename='aboutus')
router.register(r'join-us', JoinUsViewSet, basename='joinus')
router.register(r'favorites', FavoriteViewSet, basename='favorite')
router.register(r'favorite-items', FavoriteItemViewSet, basename='favoriteitem')
router.register(r'course-reviews', CourseReviewViewSet, basename='coursereview')

urlpatterns = [
    path('', include(router.urls)),
]
