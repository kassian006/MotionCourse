from .views import *
from django.urls import path,include
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'users', UserProfileViewSet, basename='users'),

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('students/', StudentListAPIView.as_view(), name='students_list'),
    path('owner/', OwnerListAPIView.as_view(), name='owner_list'),
]