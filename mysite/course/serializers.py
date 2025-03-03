from .models import *
from rest_framework import serializers


class MainCourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCourse
        fields = '__all__'

class MainCourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCourse
        fields = '__all__'


class FavoriteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'


class FavoriteDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'


class FavoriteItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteItem
        fields = '__all__'


class FavoriteItemDetailSerializer(serializers.ModelSerializer):
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
