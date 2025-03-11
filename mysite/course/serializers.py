from .models import *
from rest_framework import serializers
# from users.serializers import StudentListSerializer


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
    good_check = serializers.SerializerMethodField()
    time = serializers.TimeField(format('%H:%M'))
    category = CategorySerializer(read_only=True)

    class Meta:
        model = MainCourse
        fields = ['category_id', 'course_img', 'category', 'title', 'description', 'status', 'time', 'count_lessons', 'price', 'good_check']

    def get_good_check(self, obj):
        return obj.get_good_check()


class VideoCourseReviewCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = VideoCourseReview
        fields = '__all__'


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


class LessonCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


class LessonSimpleSerializer(serializers.ModelSerializer):
    name_lesson = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        fields = ['title', 'name_lesson']

    def get_name_lesson(self, obj):
        return str(obj.name_lesson)


class VideoCourseCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = VideoCourse
        fields = '__all__'


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


class AboutUsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'

class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ['img', 'about_owner']


class FavoriteSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = Favorite
        fields = ['user', 'created_date']

    def get_user(self, obj):
        return str(obj.user)

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
    student = serializers.SerializerMethodField()
    course = serializers.SerializerMethodField()
    created_date = serializers.DateTimeField(format='%d-%m-%Y')
    class Meta:
        model = CourseReview
        fields = ['student', 'course', 'text', 'stars', 'created_date']

    def get_student(self, obj):
        return str(obj.student)

    def get_course(self, obj):
        return str(obj.course)


class CourseReviewDetailSerializer(serializers.ModelSerializer):
    student = serializers.SerializerMethodField()
    course = serializers.SerializerMethodField()
    created_date = serializers.DateTimeField(format='%d-%m-%Y')

    class Meta:
        model = CourseReview
        fields = ['student', 'course', 'text', 'stars', 'created_date']

    def get_student(self, obj):
        return str(obj.student)

    def get_course(self, obj):
        return str(obj.course)
