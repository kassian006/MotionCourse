from rest_framework import viewsets, generics, status, filters
from rest_framework.response import Response
from .models import *
from users.models import UserProfile
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter



class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class MainCourseCreateAPIView(generics.CreateAPIView):
    queryset = MainCourse.objects.all()
    serializer_class = MainCourseCreateListSerializer


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


class LessonCreateAPIView(generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonCreateSerializer


class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonVideoRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonDetailSerializer


class VideoCourseCreateAPIView(generics.CreateAPIView):
    queryset = VideoCourse.objects.all()
    serializer_class = VideoCourseCreateSerializer


class VideoCourseRetrieveAPIView(generics.RetrieveAPIView):
    queryset = VideoCourse.objects.all()
    serializer_class = VideoCourseSerializer


class AboutUsListAPIView(generics.ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer


class AboutUsCreateAPIView(generics.CreateAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsCreateSerializer


class JoinUsCreateAPIView(generics.CreateAPIView):
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

    # def get_queryset(self):
    #     return Favorite.objects.filter(user__id=self.request.user.id)


class CourseReviewListAPIView(generics.ListAPIView):
    queryset = CourseReview.objects.all()
    serializer_class = CourseReviewListSerializer


class CourseRetrieveDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CourseReview.objects.all()
    serializer_class = CourseReviewDetailSerializer


class CourseReviewCreateAPIView(generics.CreateAPIView):
    queryset = CourseReview.objects.all()
    serializer_class = CourseReviewCreateSerializer


class VideoCourseReviewListAPIView(generics.ListAPIView):
    queryset = VideoCourseReview.objects.all()
    serializer_class = VideoCourseReviewListSerializer


class VideoCourseReviewCreateAPIView(generics.CreateAPIView):
    queryset = VideoCourseReview.objects.all()
    serializer_class = VideoCourseReviewCreateSerializer
