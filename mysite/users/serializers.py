from .models import *
from rest_framework import serializers


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
        fields = ['bio', 'student_image']


class TeacherListSerializer(serializers.ModelSerializer):
    teacher_image = serializers.ImageField(source='user.profile.image', read_only=True)

    class Meta:
        model = Teacher
        fields = ['id', 'teacher_image']


class TeacherDetailSerializers(serializers.ModelSerializer):
    teacher_image = serializers.ImageField(source='user.profile.image', read_only=True)

    class Meta:
        model = UserProfile
        fields = ['teacher_image']
