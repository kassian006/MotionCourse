from .models import *
from rest_framework import serializers

from users.models import Student


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

class MainCourseSimpleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = MainCourse
        fields = ['title', 'description', 'status',]


class MainCourseListSerializer(serializers.ModelSerializer):
    time = serializers.TimeField(format='%H:%M')
    category = CategorySerializer(read_only=True)
    good_check = serializers.SerializerMethodField()
    class Meta:
        model = MainCourse
        fields = ['course_img', 'category', 'title', 'description', 'status', 'time', 'count_lessons', 'price', 'good_check']

    def get_good_check(self, obj):
        return  obj.get_good_check()

class VideoCourseReviewCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = VideoCourseReview
        fields = '__all__'


class VideoCourseSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoCourse
        fields = ['id','lesson', 'course_video', 'created_date', 'time']



class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'username']
        ref_name = 'CourseStudentList'  # Уникальное имя схемы для course.serializers


class VideoCourseReviewListSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)
    view_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)
    video = VideoCourseSimpleSerializer(read_only=True)
    student = StudentListSerializer(read_only=True)

    class Meta:
        model = VideoCourseReview
        fields = ['student', 'text', 'video', 'created_date', 'view_date', 'parent']


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
    lesson = LessonSimpleSerializer(read_only=True)  # Используйте 'lesson' напрямую
    created_date = serializers.DateField(format='%d-%m-%Y')
    time = serializers.TimeField(format='%H:%M')
    video_review = VideoCourseReviewListSerializer(read_only=True)

    class Meta:
        model = VideoCourse
        fields = ['id', 'lesson', 'created_date', 'time', 'video_review', 'course_video', 'title']



class LessonSerializer(serializers.ModelSerializer):
    name_lesson = MainCourseSimpleListSerializer(read_only=True)
    course_videos = VideoCourseSerializer(read_only=True, many=True)

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
