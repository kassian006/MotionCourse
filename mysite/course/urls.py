from django.urls import path, include
from rest_framework.routers import  SimpleRouter
from .views import (
    CategoryListAPIView,
    MainCourseListAPIView,
    LessonListAPIView,
    FavoriteViewSet,
    FavoriteItemViewSet,
    CourseReviewListAPIView,
    VideoCourseRetrieveAPIView,
    MainCourseCreateAPIView,
    LessonCreateAPIView,
    VideoCourseCreateAPIView,
    AboutUsCreateAPIView,
    AboutUsListAPIView,
    JoinUsCreateAPIView,
    CourseReviewCreateAPIView,
    CourseRetrieveDestroyAPIView,
    VideoCourseReviewListAPIView,
    VideoCourseReviewCreateAPIView
)

router = SimpleRouter()
router.register(r'favorites', FavoriteViewSet, basename='favorite')
router.register(r'favorite-items', FavoriteItemViewSet, basename='favoriteitem')

urlpatterns = [
    path('', include(router.urls)),
    path('main_courses/', MainCourseListAPIView.as_view(), name='main_courses'),
    path('main_courses/create', MainCourseCreateAPIView.as_view(), name='main_courses_create'),
    path('lessons/', LessonListAPIView.as_view(), name='lessons'),
    path('lessons/create', LessonCreateAPIView.as_view(), name='lessons_create'),
    path('lessons/<int:pk>/', VideoCourseRetrieveAPIView.as_view(), name='lessons_detail'),
    path('videos/create', VideoCourseCreateAPIView.as_view(), name='lessons_create'),
    path('categories/', CategoryListAPIView.as_view(), name='categories'),
    path('about_us/', AboutUsListAPIView.as_view(), name='about_us'),
    path('about_us/create', AboutUsCreateAPIView.as_view(), name='about_us_create'),
    path('join_us/', JoinUsCreateAPIView.as_view(), name='about_us'),
    path('course_reviews/', CourseReviewListAPIView.as_view(), name='course_reviews'),
    path('course_reviews/create', CourseReviewCreateAPIView.as_view(), name='course_reviews_create'),
    path('course_reviews/<int:pk>/', CourseRetrieveDestroyAPIView.as_view(), name='course_reviews_edit'),
    path('video_reviews/', VideoCourseReviewListAPIView.as_view(), name='video_reviews'),
    path('video_reviews/create', VideoCourseReviewCreateAPIView.as_view(), name='video_reviews_create'),

]
