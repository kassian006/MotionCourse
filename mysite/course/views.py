from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from .models import *
from users.models import UserProfile
from .serializers import *


class MainCourseListViewSet(viewsets.ModelViewSet):
    queryset = MainCourse.objects.all()
    serializer_class = MainCourseListSerializer


class MainCourseDetailViewSet(viewsets.ModelViewSet):
    queryset = MainCourse.objects.all()
    serializer_class = MainCourseDetailSerializer


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = MainCourse.objects.all()
    serializer_class = FavoriteSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


class FavoriteItemViewSet(viewsets.ModelViewSet):
    queryset = FavoriteItem.objects.all()
    serializer_class = FavoriteItemSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


class CourseReviewListViewSet(viewsets.ModelViewSet):
    queryset = CourseReview.objects.all()
    serializer_class = CourseReviewListSerializer


class CourseReviewDetailViewSet(viewsets.ModelViewSet):
    queryset = CourseReview.objects.all()
    serializer_class = CourseReviewDetailSerializer