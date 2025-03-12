# Generated by Django 5.1.6 on 2025-03-12 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_initial'),
        ('users', '0002_remove_student_student_course'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Student', 'verbose_name_plural': 'Students'},
        ),
        migrations.AddField(
            model_name='student',
            name='purchased_courses',
            field=models.ManyToManyField(related_name='students', to='course.maincourse'),
        ),
    ]
