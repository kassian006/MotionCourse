from django.contrib.auth import authenticate
from .models import *
from course.serializers import MainCourseListSerializer
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance. username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }



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
