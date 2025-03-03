from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from .models import *
from .serializers import *


class MainCourseListViewSet(viewsets.ModelViewSet):
    queryset = MainCourse.objects.all()
    serializer_class = MainCourseListSerializer


class MainCourseDetailViewSet(viewsets.ModelViewSet):
    queryset = MainCourse.objects.all()
    serializer_class = MainCourseDetailSerializer


class FavoriteListViewSet(viewsets.ModelViewSet):
    queryset = MainCourse.objects.all()
    serializer_class = FavoriteListSerializer


class FavoriteDetailViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteDetailSerializer


class FavoriteItemListViewSet(viewsets.ModelViewSet):
    queryset = FavoriteItem.objects.all()
    serializer_class = FavoriteItemListSerializer


class FavoriteItemDetailViewSet(viewsets.ModelViewSet):
    queryset = FavoriteItem.objects.all()
    serializer_class = FavoriteItemDetailSerializer


class CourseReviewListViewSet(viewsets.ModelViewSet):
    queryset = CourseReview.objects.all()
    serializer_class = CourseReviewListSerializer


class CourseReviewDetailViewSet(viewsets.ModelViewSet):
    queryset = CourseReview.objects.all()
    serializer_class = CourseReviewDetailSerializer