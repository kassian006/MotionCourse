from .models import *
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
    student_image = serializers.ImageField(source='user.profile.image', read_only=True)


    class Meta:
        model = Student
        fields = ['id','student_image']


class StudentDetailSerializer(serializers.ModelSerializer):
    student_image = serializers.ImageField(source='user.profile.image', read_only=True)


    class Meta:
        model = Student
        fields = ['student_image', 'background', 'first_name', 'last_name', 'status']


class OwnerListSerializer(serializers.ModelSerializer):
    owner_image = serializers.ImageField(source='user.profile.image', read_only=True)

    class Meta:
        model = Owner
        fields = ['id', 'owner_image']


class OwnerDetailSerializers(serializers.ModelSerializer):
    owner_image = serializers.ImageField(source='user.profile.image', read_only=True)

    class Meta:
        model = Owner
        fields = ['owner_image', 'background', 'first_name', 'last_name', 'status']
