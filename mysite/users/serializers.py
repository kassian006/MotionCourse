from .models import *
from course.serializers import MainCourseListSerializer
from rest_framework import serializers


class CountryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id','country_name']


class CountryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name']


class CityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id','city_name']


class CityDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['city_name']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']


class StudentListSerializer(serializers.ModelSerializer):
    my_course = MainCourseListSerializer()
    class Meta:
        model = Student
        fields = ['profile_picture', 'background', 'first_name', 'last_name', 'status', 'my_course']


class OwnerListSerializer(serializers.ModelSerializer):
    owner_course = MainCourseListSerializer()
    class Meta:
        model = Owner
        fields = ['profile_picture', 'background', 'first_name', 'last_name', 'status', 'owner_course']
