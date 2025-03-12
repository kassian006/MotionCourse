from rest_framework import viewsets, generics, status, filters, permissions
from .serializers import (
    JoinUsSerializer,
    CategorySerializer,
    MainCourseCreateListSerializer,
    MainCourseListSerializer,
    VideoCourseReviewCreateSerializer,
    VideoCourseSimpleSerializer,
    VideoCourseReviewListSerializer,
    LessonCreateSerializer,
    LessonSimpleSerializer,
    VideoCourseCreateSerializer,
    VideoCourseSerializer,
    LessonSerializer,
    MainCourseLessonsSerializer,
    LessonDetailSerializer,
    AboutUsCreateSerializer,
    AboutUsSerializer,
    FavoriteSerializer,
    FavoriteItemSerializer,
    CourseReviewCreateSerializer,
    CourseReviewListSerializer,
    CourseReviewDetailSerializer
)
from .models import *
from users.models import UserProfile
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .permissions import CheckEditOwner, CheckStatusCreate, CheckStudentReview




class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class MainCourseCreateAPIView(generics.CreateAPIView):
    queryset = MainCourse.objects.all()
    serializer_class = MainCourseCreateListSerializer
    permission_classes = [CheckStatusCreate]

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


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
    permission_classes = [CheckStatusCreate]

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [CheckEditOwner]

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


class VideoCourseAPIView(generics.ListAPIView):
    queryset = VideoCourse.objects.all()
    serializer_class = VideoCourseSerializer


class VideoCourseCreateAPIView(generics.CreateAPIView):
    queryset = VideoCourse.objects.all()
    serializer_class = VideoCourseCreateSerializer
    permission_classes = [CheckStatusCreate]

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


class VideoCourseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VideoCourse.objects.all()
    serializer_class = VideoCourseSerializer
    permission_classes = [CheckEditOwner]

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


class AboutUsListAPIView(generics.ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer


class AboutUsCreateAPIView(generics.CreateAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsCreateSerializer
    permission_classes = [CheckStatusCreate]

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


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

    def get_queryset(self):
        return Favorite.objects.filter(user__id=self.request.user.id)


class CourseReviewListAPIView(generics.ListAPIView):
    queryset = CourseReview.objects.all()
    serializer_class = CourseReviewListSerializer


class CourseRetrieveDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CourseReview.objects.all()
    serializer_class = CourseReviewDetailSerializer
    permission_classes = [CheckStudentReview]

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


class CourseReviewCreateAPIView(generics.CreateAPIView):
    queryset = CourseReview.objects.all()
    serializer_class = CourseReviewCreateSerializer
    permission_classes = [CheckStudentReview]

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


class VideoCourseReviewListAPIView(generics.ListAPIView):
    queryset = VideoCourseReview.objects.all()
    serializer_class = VideoCourseReviewListSerializer


class VideoCourseReviewCreateAPIView(generics.CreateAPIView):
    queryset = VideoCourseReview.objects.all()
    serializer_class = VideoCourseReviewCreateSerializer
    permission_classes = [CheckStudentReview]

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


