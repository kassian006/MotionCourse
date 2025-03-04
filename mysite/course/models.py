from django.db import models
from django.db.models import Avg
from users.models import UserProfile, Student, Owner, Country, City

STATUS_COURSE_CHOICES = (
    ('free', 'free'),
    ('paid', 'paid'),
    ('mine', 'mine')
)


class MainCourse(models.Model):
    title = models.CharField(max_length=512)
    description = models.TextField()
    course_img = models.ImageField(upload_to='course_img/')
    status = models.CharField(choices=STATUS_COURSE_CHOICES, max_length=64)
    time = models.TimeField()
    # user_course = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_course')
    count_lessons = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.title

    def get_good_check(self):
        leader_rating = self.reviews_course.all()
        if leader_rating.exists():
            avg_rating = leader_rating.aggregate(Avg('stars'))['stars__avg']
            if avg_rating >= 4:
                return 'Прогресс'
        return False



class Favorite(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='favorite_user')
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
    stars = models.DecimalField(choices=[(i, str(i)) for i in range(1, 6)],
                                verbose_name='рейтинг', max_digits=2, decimal_places=1)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.student}, - {self.stars}'
