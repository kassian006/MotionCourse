from django.db import models
from django.contrib.auth.models import AbstractUser
from course.models import *


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
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
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


class Owner(UserProfile):
    pass

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

    class Meta:
        verbose_name = 'Owner'
        verbose_name_plural = 'Owner'
