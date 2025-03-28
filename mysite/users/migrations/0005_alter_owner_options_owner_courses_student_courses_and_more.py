# Generated by Django 5.1.6 on 2025-03-13 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_alter_videocourse_created_date'),
        ('users', '0004_remove_student_purchased_courses_purchasedcourse'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='owner',
            options={'verbose_name': 'Owner', 'verbose_name_plural': 'Owners'},
        ),
        migrations.AddField(
            model_name='owner',
            name='courses',
            field=models.ManyToManyField(related_name='owners', to='course.maincourse'),
        ),
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(related_name='students', to='course.maincourse'),
        ),
        migrations.DeleteModel(
            name='PurchasedCourse',
        ),
    ]
