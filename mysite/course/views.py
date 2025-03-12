from rest_framework import viewsets, generics, status, filters
from rest_framework.response import Response
from .models import *
from users.models import UserProfile
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class MainCourseListAPIView(generics.ListAPIView):
    queryset = MainCourse.objects.all()
    serializer_class = MainCourseListSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['status']  # Фильтр по статусу

    def get_queryset(self):
        queryset = MainCourse.objects.all()
        filter_type = self.request.query_params.get('type')

        if filter_type == 'free':
            return queryset.filter(status='free')
        elif filter_type == 'paid':
            return queryset.filter(status='paid')
        elif filter_type == 'mine':
            return queryset.filter(status='mine')
        return queryset  # Если нет параметра, возвращаем все курсы

class CourseLessonListAPIView(generics.ListAPIView):
    queryset = MainCourse.objects.all()
    serializer_class = MainCourseLessonsSerializer


class LessonVideoRetrieveAPIView(generics.RetrieveAPIView):
    queryset = MainCourse.objects.all()
    serializer_class = LessonDetailSerializer


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class VideoCourseRetrieveAPIView(generics.RetrieveAPIView):
    queryset = VideoCourse.objects.all()
    serializer_class = VideoCourseSerializer


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


class VideoCourseReviewViewSet(viewsets.ModelViewSet):
    queryset = VideoCourseReview.objects.all()
    serializer_class = VideoCourseReviewListSerializer
