from .views import *
from django.urls import path,include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserProfileViewSet, basename='users'),

urlpatterns = [
    path('', include(router.urls)),
    path('students/', StudentListAPIView.as_view(), name='students_list'),
    path('students/<int:pk>/', StudentDetailAPIView.as_view(), name='students_detail'),

    path('teacher/', TeacherListAPIView.as_view(), name='teacher_list'),
    path('teacher/<int:pk>/', TeacherDetailAPIView.as_view(), name='teacher_detail'),

]