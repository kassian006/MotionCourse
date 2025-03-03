from .views import *
from django.urls import path,include
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'users', UserProfileViewSet, basename='users'),

urlpatterns = [
    path('', include(router.urls)),
    path('students/', StudentListAPIView.as_view(), name='students_list'),
    path('students/<int:pk>/', StudentDetailAPIView.as_view(), name='students_detail'),

    path('owner/', OwnerListAPIView.as_view(), name='owner_list'),
    path('owner/<int:pk>/', OwnerDetailAPIView.as_view(), name='owner_detail'),

]