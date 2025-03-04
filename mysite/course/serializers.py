from .models import *
from rest_framework import serializers


class MainCourseListSerializer(serializers.ModelSerializer):
    good_check = serializers.SerializerMethodField()
    time = serializers.TimeField(format('%H:%M'))

    class Meta:
        model = MainCourse
        fields = '__all__'

    def get_good_check(self, obj):
        return obj.get_good_check()

class MainCourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCourse
        fields = '__all__'


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'


class FavoriteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteItem
        fields = '__all__'


class CourseReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseReview
        fields = '__all__'


class CourseReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteItem
        fields = '__all__'
