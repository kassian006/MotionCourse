from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField




class UserProfile(AbstractUser):
    address = models.CharField(max_length=54)
    age = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(18), MaxValueValidator(70)
    ], null=True, blank=True)
    bio = models.TextField()
    data_birth = models.DateField(null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', null=True, blank=True)
    # status = models.CharField(max_length=16, choices=STATUS_CHOICES, default='student')


    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
