from rest_framework import viewsets, generics, status
from users.models import UserProfile
from .serializers import *


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class MainCourseViewSet(viewsets.ModelViewSet):
    queryset = MainCourse.objects.all()
    serializer_class = MainCourseListSerializer


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class AboutUsViewSet(viewsets.ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer


class JoinUsViewSet(viewsets.ModelViewSet):
    queryset = JoinUs.objects.all()
    serializer_class = JoinUsSerializer


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    def get_queryset(self):
        return Favorite.objects.filter(user__id=self.request.user.id)


class FavoriteItemViewSet(viewsets.ModelViewSet):
    queryset = FavoriteItem.objects.all()
    serializer_class = FavoriteItemSerializer

    def get_queryset(self):
        return Favorite.objects.filter(user__id=self.request.user.id)


class CourseReviewViewSet(viewsets.ModelViewSet):
    queryset = CourseReview.objects.all()
    serializer_class = CourseReviewListSerializer
