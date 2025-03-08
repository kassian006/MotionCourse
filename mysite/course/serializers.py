from .models import *
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']


class MainCourseListSerializer(serializers.ModelSerializer):
    good_check = serializers.SerializerMethodField()
    time = serializers.TimeField(format('%H:%M'))

    class Meta:
        model = MainCourse
        fields = ['course_img', 'title', 'description', 'status', 'time', 'count_lessons', 'price', 'good_check']

    def get_good_check(self, obj):
        return obj.get_good_check()


class VideoCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoCourse
        fields = ['course_video']


class LessonSerializer(serializers.ModelSerializer):
    video_lessons = VideoCourseSerializer(many=True, read_only=True)
    class Meta:
        model = Lesson
        fields = ['name_lesson', 'video_lessons', 'title']

    def get_good_check(self, obj):
        return obj.get_good_check()

class MainCourseDetailSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(many=True, read_only=True)
    class Meta:
        model = MainCourse
        fields = ['course_img', 'title', 'description', 'status', 'time', 'count_lessons', 'price']


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ['img', 'about_owner']


class JoinUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = JoinUs
        fields = ['email']


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['user', 'created_date']


class FavoriteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteItem
        fields = ['course', 'favorite']


class CourseReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseReview
        fields = '__all__'


class CourseReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteItem
        fields = '__all__'
