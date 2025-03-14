from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


def get_student_courses():
    from course.models import MainCourse
    # Используйте MainCourse здесь


STATUS_CHOICES = (
    ('admin', 'admin'),
    ('student', 'student'),
    ('owner', 'owner'),
)

class Country(models.Model):
    country_name = models.CharField(max_length=65, null=True, blank=True)

    def __str__(self):
        return self.country_name


class City(models.Model):
    city_name = models.CharField(max_length=65, null=True, blank=True)

    def __str__(self):
        return self.city_name


class UserProfile(AbstractUser):
    email = models.EmailField(unique=True)  # Делаем email уникальным
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    background = models.FileField(upload_to='background/', null=True, blank=True)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'


class Student(UserProfile):
    courses = models.ManyToManyField('course.MainCourse', related_name='students')
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default='student')

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'


class Owner(UserProfile):
    courses = models.ManyToManyField('course.MainCourse', related_name='owners')
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default='owner')

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

    class Meta:
        verbose_name = 'Owner'
        verbose_name_plural = 'Owners'

class Cart(models.Model):
    user = models.OneToOneField(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    order_course = models.ForeignKey('course.MainCourse', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.cart} - {self.order_course}'


 # THIS CHAT

class Group(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room_group_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='image_group/', null=True, blank=True)

    def __str__(self):
        return f'{self.room_group_name}'


class GroupMember(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="members")
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='group_member')
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.users} in {self.group}"


class Message(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='messages')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='message_image', null=True, blank=True)
    video = models.FileField(upload_to='message_video', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"{self.author} in {self.group}"


