from .models import *
from rest_framework import serializers


class JoinUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = JoinUs
        fields = ['email']

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


class VideoCourseReviewListSerializer(serializers.ModelSerializer):
    student = serializers.SerializerMethodField()
    created_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    view_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    video = serializers.SerializerMethodField()

    class Meta:
        model = VideoCourseReview
        fields = ['student', 'video', 'text', 'created_date', 'view_date', 'parent']

    def get_student(self, obj):
        return str(obj.student)

    def get_video(self, obj):
        return str(obj.video)


class LessonSimpleSerializer(serializers.ModelSerializer):
    name_lesson = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        fields = ['title', 'name_lesson']

    def get_name_lesson(self, obj):
        return str(obj.name_lesson)


class VideoCourseSerializer(serializers.ModelSerializer):
    lesson = LessonSimpleSerializer()
    created_date = serializers.DateTimeField(format='%d-%m-%Y')
    time = serializers.TimeField(format='%H:%M')
    views = serializers.SerializerMethodField()
    video_review = VideoCourseReviewListSerializer(many=True, read_only=True, source='reviews_video')

    class Meta:
        model = VideoCourse
        fields = ['lesson', 'course_video', 'created_date', 'time', 'views', 'video_review']

    def get_views(self, obj):
        return JoinUs.objects.count()


class LessonSerializer(serializers.ModelSerializer):
    name_lesson = serializers.SerializerMethodField()
    course_videos = VideoCourseSerializer(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = ['course_videos', 'title', 'name_lesson']

    def get_name_lesson(self, obj):
        return str(obj.name_lesson)


class MainCourseLessonsSerializer(serializers.ModelSerializer):
    name_lessons = LessonSerializer(many=True, read_only=True)
    class Meta:
        model = MainCourse
        fields = ['course_img', 'title', 'description', 'status', 'time', 'count_lessons', 'price', 'name_lessons']


class LessonDetailSerializer(serializers.ModelSerializer):
    name_lessons = LessonSerializer(many=True, read_only=True)
    class Meta:
        model = Lesson
        fields = ['name_lessons']


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ['img', 'about_owner']




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
