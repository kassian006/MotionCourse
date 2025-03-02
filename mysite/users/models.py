from django.db import models
from django.contrib.auth.models import AbstractUser

STATUS_CHOICES = (
    ('admin', 'admin'),
    ('student', 'student'),
    ('teacher', 'teacher'),
)


class UserProfile(AbstractUser):
    country = models.CharField(max_length=66, unique=True)
    city = models.CharField(max_length=65, unique=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    background = models.FileField(upload_to='background/', null=True, blank=True)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default='student')


    def __str__(self):
        return f'{self.last_name}, {self.first_name}'


class Student(UserProfile):
    pass

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Student'


class Teacher(UserProfile):
    pass

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teacher'
