from .models import *
from rest_framework import serializers
# from mysite.users.serializers import StudentListSerializer, UserProfileSimpleSerializer



class JoinUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = JoinUs
        fields = ['email']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']


class MainCourseCreateListSerializer(serializers.ModelSerializer):

    class Meta:
        model = MainCourse
        fields = '__all__'


class MainCourseListSerializer(serializers.ModelSerializer):
    time = serializers.TimeField(format='%H:%M')
    category = CategorySerializer(read_only=True)

    class Meta:
        model = MainCourse
        fields = ['category_id', 'course_img', 'category', 'title', 'description', 'status', 'time', 'count_lessons', 'price',]


class VideoCourseReviewCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = VideoCourseReview
        fields = '__all__'


class VideoCourseSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoCourse
        fields = ['id','lesson', 'course_video', 'created_date', 'time']



class VideoCourseReviewListSerializer(serializers.ModelSerializer):
    # student = StudentListSerializer()
    created_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    view_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    video = VideoCourseSimpleSerializer()

    class Meta:
        model = VideoCourseReview
        fields = ['student', 'video', 'text', 'created_date', 'view_date', 'parent']


class LessonCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


class LessonSimpleSerializer(serializers.ModelSerializer):
    name_lesson = MainCourseListSerializer()

    class Meta:
        model = Lesson
        fields = ['title', 'name_lesson']



class VideoCourseCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = VideoCourse
        fields = '__all__'


class VideoCourseSerializer(serializers.ModelSerializer):
    lesson = LessonSimpleSerializer()
    created_date = serializers.DateTimeField(format='%d-%m-%Y')
    time = serializers.TimeField(format='%H:%M')
    video_review = VideoCourseReviewListSerializer( read_only=True, source='reviews_video')

    class Meta:
        model = VideoCourse
        fields = ['id','lesson', 'course_video', 'created_date', 'time', 'video_review']



class LessonSerializer(serializers.ModelSerializer):
    name_lesson = LessonSimpleSerializer()
    course_videos = VideoCourseSerializer(read_only=True)

    class Meta:
        model = Lesson
        fields = ['id', 'course_videos', 'title', 'name_lesson']


class MainCourseLessonsSerializer(serializers.ModelSerializer):
    name_lessons = LessonSerializer(read_only=True)
    class Meta:
        model = MainCourse
        fields = ['course_img', 'title', 'description', 'status', 'time', 'count_lessons', 'price', 'name_lessons']


class LessonDetailSerializer(serializers.ModelSerializer):
    name_lessons = LessonSerializer(read_only=True)
    class Meta:
        model = Lesson
        fields = ['name_lessons']


class AboutUsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'

class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ['img', 'about_owner']


class FavoriteSerializer(serializers.ModelSerializer):
    # user = UserProfileSimpleSerializer()
    class Meta:
        model = Favorite
        fields = ['user', 'created_date']


class FavoriteItemSerializer(serializers.ModelSerializer):
    course = MainCourseListSerializer()
    favorite = FavoriteSerializer()
    class Meta:
        model = FavoriteItem
        fields = ['course', 'favorite']


class CourseReviewCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseReview
        fields = '__all__'


class CourseReviewListSerializer(serializers.ModelSerializer):
    # student = StudentListSerializer()
    course = MainCourseListSerializer()
    created_date = serializers.DateTimeField(format='%d-%m-%Y')
    class Meta:
        model = CourseReview
        fields = ['id', 'student', 'course', 'text', 'stars', 'created_date']


class CourseReviewDetailSerializer(serializers.ModelSerializer):
    # student = StudentListSerializer()
    course = MainCourseListSerializer()
    created_date = serializers.DateTimeField(format='%d-%m-%Y')

    class Meta:
        model = CourseReview
        fields = ['student', 'course', 'text', 'stars', 'created_date']
