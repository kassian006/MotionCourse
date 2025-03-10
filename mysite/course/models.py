from django.db import models
from django.db.models import Avg
from users.models import UserProfile, Student, Owner, Country, City
from decimal import Decimal
from datetime import time
from django.core.exceptions import ValidationError



STATUS_COURSE_CHOICES = (
    ('free', 'free'),
    ('paid', 'paid'),
    ('mine', 'mine')
)

class Category(models.Model):
    category_name = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.category_name}'


class MainCourse(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=512)
    description = models.TextField()
    course_img = models.ImageField(upload_to='course_img/')
    status = models.CharField(choices=STATUS_COURSE_CHOICES, max_length=64)
    time = models.TimeField()
    # user_course = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_course')
    count_lessons = models.PositiveSmallIntegerField()
    price = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.category} - {self.title} - {self.status}'

    def get_good_check(self):
        leader_rating = self.reviews_course.all()
        if leader_rating.exists():
            avg_rating = leader_rating.aggregate(Avg('stars'))['stars__avg']
            if avg_rating >= 4:
                return 'Прогресс'
        return False


class Lesson(models.Model):
    name_lesson = models.ForeignKey(MainCourse, on_delete=models.CASCADE, related_name='name_lessons')
    title = models.CharField(max_length=512)

    def __str__(self):
        return f'{self.name_lesson} - {self.title}'


class VideoCourse(models.Model):
    time = models.TimeField()
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='course_videos')
    course = models.ForeignKey(MainCourse, on_delete=models.CASCADE)
    course_video = models.FileField(upload_to='course_video/')
    title = models.CharField(max_length=1028)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.lesson} - {self.course}'


class Favorite(models.Model):
    user = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='favorite_user', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.created_date}'


class FavoriteItem(models.Model):
    course = models.ForeignKey(MainCourse, on_delete=models.CASCADE, related_name='course_favorite')
    favorite = models.ForeignKey(Favorite, on_delete=models.CASCADE, related_name='favorite_item')

    def __str__(self):
        return f'{self.course} - {self.favorite}'


class CourseReview(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(MainCourse, on_delete=models.CASCADE, related_name='reviews_course')
    text = models.TextField()
    stars = models.DecimalField(choices=[(Decimal(i), str(i)) for i in range(1, 6)],
                                verbose_name='рейтинг', max_digits=2, decimal_places=1)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.student}, - {self.stars}'


class VideoCourseReview(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    video = models.ForeignKey(VideoCourse, on_delete=models.CASCADE, related_name='reviews_video')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    view_date = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.student}, - {self.text}'


class AboutUs(models.Model):
    img = models.ImageField(upload_to='owner_img')
    about_owner = models.TextField()

    def __str__(self):
        return f'{self.about_owner}'


class JoinUs(models.Model):
    email = models.EmailField()

    def __str__(self):
        return f'{self.email}'
