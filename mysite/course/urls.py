from django.urls import path, include
from rest_framework.routers import  SimpleRouter
from .views import (
    CategoryViewSet,
    MainCourseListAPIView,
    CourseLessonListAPIView,
    LessonViewSet,
    AboutUsViewSet,
    JoinUsViewSet,
    FavoriteViewSet,
    FavoriteItemViewSet,
    CourseReviewViewSet,
    VideoCourseRetrieveAPIView,
    VideoCourseReviewViewSet
)

router = SimpleRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'lessons', LessonViewSet, basename='lesson')
router.register(r'about-us', AboutUsViewSet, basename='aboutus')
router.register(r'join-us', JoinUsViewSet, basename='joinus')
router.register(r'favorites', FavoriteViewSet, basename='favorite')
router.register(r'favorite-items', FavoriteItemViewSet, basename='favoriteitem')
router.register(r'course-reviews', CourseReviewViewSet, basename='coursereview')
router.register(r'video_reviews', VideoCourseReviewViewSet, basename='video_reviews')

urlpatterns = [
    path('', include(router.urls)),
    path('main_courses/', MainCourseListAPIView.as_view(), name='main_courses'),
    path('main_courses/lessons/', CourseLessonListAPIView.as_view(), name='main_courses_lessons'),
    path('main_courses/lessons/<int:pk>/', VideoCourseRetrieveAPIView.as_view(), name='main_courses_detail'),

]
