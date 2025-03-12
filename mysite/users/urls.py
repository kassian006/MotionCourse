from .views import *
from django.urls import path,include
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'users', UserProfileViewSet, basename='users'),

urlpatterns = [
    path('', include(router.urls)),
    path('password_reset/verify_code/', verify_reset_code, name='verify_reset_code'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('students/', StudentListAPIView.as_view(), name='students_list'),
    path('students/<int:pk>/', StudentDetailAPIView.as_view(), name='students_detail'),
    path('student_register/', StudentRegisterAPIView.as_view(), name='students_register'),
    path('owner/', OwnerListAPIView.as_view(), name='owner_list'),
    path('owner/<int:pk>/', OwnerDetailAPIView.as_view(), name='owner_detail'),
    path('group/<int:group_id>/remove_user/<int:user_id>/', RemoveUserFromGroupView.as_view(),
         name='remove_user_from_group'),
    path('user/', GroupMemberView.as_view(), name='user_list'),
    path('user/<int:pk>/', GroupMemberRetrieve.as_view(), name='user_detail'),
    path('groups/', GroupListCreateView.as_view(), name='group-list-create'),
    path('groups/<int:pk>/', GroupDetailView.as_view(), name='group-detail'),
    path('group_members/', GroupMemberView.as_view(), name='group_member-list'),
    path('group_members/<int:pk>/', GroupMemberRetrieve.as_view(), name='group_member-detail'),
    path('messages/', MessageListCreateView.as_view(), name='message-list-create'),
    path('messages/<int:pk>/', MessageDetailView.as_view(), name='message-detail'),

]