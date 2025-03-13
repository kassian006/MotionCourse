from django.contrib.auth import authenticate
from .models import *
from course.serializers import MainCourseListSerializer
from course.models import MainCourse
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django_rest_passwordreset.models import ResetPasswordToken



class VerifyResetCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()  # Email пользователя
    reset_code = serializers.IntegerField()  # 4-значный код
    new_password = serializers.CharField(write_only=True)  # Новый пароль

    def validate(self, data):
        email = data.get('email')
        reset_code = data.get('reset_code')

        # Проверяем, существует ли указанный код для email
        try:
            token = ResetPasswordToken.objects.get(user__email=email, key=reset_code)
        except ResetPasswordToken.DoesNotExist:
            raise serializers.ValidationError("Неверный код сброса или email.")

        data['user'] = token.user
        return data

    def save(self):
        user = self.validated_data['user']
        new_password = self.validated_data['new_password']

        # Устанавливаем новый пароль
        user.set_password(new_password)
        user.save()


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
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        user = UserProfile.objects.filter(email=email).first()
        if not user:
            raise serializers.ValidationError("Пользователь с таким email не найден")
        user = authenticate(username=user.username, password=password)
        if not user:
            raise serializers.ValidationError("Неверные учетные данные")
        return user

    # def validate(self, data):
    #     user = authenticate(**data)
    #     if user and user.is_active:
    #         return user
    #     raise serializers.ValidationError("Неверные учетные данные")

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

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()


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
        fields = ['first_name', 'last_name', 'profile_picture']


class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'profile_picture', 'background', 'first_name', 'last_name']

class StudentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['id', 'profile_picture', 'first_name', 'last_name']


class StudentEditSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['profile_picture', 'background', 'first_name', 'last_name']


class CartCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    user = UserProfileSimpleSerializer()
    class Meta:
        model = Cart
        fields = ['id', 'user']


class CartItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    cart = CartSerializer()
    order_course = MainCourseListSerializer()
    class Meta:
        model = CartItem
        fields = ['cart', 'order_course']


class OwnerListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Owner
        fields = ['id', 'profile_picture', 'background', 'first_name', 'last_name', 'status']


class OwnerDetailSerializer(serializers.ModelSerializer):
    # owner_course = MainCourseListSerializer()
    class Meta:
        model = Owner
        fields = ['profile_picture', 'background', 'first_name', 'last_name', 'status']



class GroupSerializer(serializers.ModelSerializer):
    author = UserProfileSerializer(read_only=True)

    class Meta:
        model = Group
        fields = ['id', 'author', 'room_group_name', 'image']


class GroupSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ['id','room_group_name', 'image']


class GroupMemberSerializer(serializers.ModelSerializer):
    users = UserProfileSimpleSerializer(many=True)
    joined_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M')

    class Meta:
        model = GroupMember
        fields = ['id', 'group', 'users', 'joined_at']


class GroupMemberSimpleSerializer(serializers.ModelSerializer):
    joined_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M')

    class Meta:
        model = GroupMember
        fields = ['id', 'joined_at']


class MessageSerializer(serializers.ModelSerializer):
    # group = GroupSimpleSerializer(read_only=True
    group = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all())  # Убрали read_only=True
    author = UserProfileSimpleSerializer(read_only=True)
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M')

    class Meta:
        model = Message
        fields = ['id', 'group', 'author', 'text', 'image', 'video', 'created_at']


class GroupDetailSerializer(serializers.ModelSerializer):
    author = UserProfileSimpleSerializer(read_only=True)
    members = GroupMemberSimpleSerializer(read_only=True)

    class Meta:
        model = Group
        fields = ['id', 'author', 'room_group_name', 'image', 'members']


class UserProfileListSerializers(serializers.ModelSerializer):
    group_member = GroupMemberSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ['username', 'group_member']

