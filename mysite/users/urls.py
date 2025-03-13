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
    path('students/', StudentListView.as_view(), name='student'),
    path('students/<int:pk>/', StudentUpdateView.as_view(), name='student-update'),
    path('all_students/', AllStudentsAPIView.as_view(), name='all_students'),
    path('owner/', OwnerListAPIView.as_view(), name='owner_list'),
    path('owner/<int:pk>/', OwnerDetailAPIView.as_view(), name='owner_detail'),
    path('cart/', CartListAPIView.as_view(), name='cart'),
    path('cart/<int:pk>/', CartRetrieveUpdateDestroyAPIView.as_view(), name='cart_detail'),
    path('cart/create/', CartCreateAPIView.as_view(), name='cart_create'),
    path('cart_item/', CartItemListAPIView.as_view(), name='cart_item'),
    path('cart_item/<int:pk>/', CartItemRetrieveUpdateDestroyAPIView.as_view(), name='cart_item_detail'),
    path('cart_item/create/', CartItemCreateAPIView.as_view(), name='cart_item_create'),

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