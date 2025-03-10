# Generated by Django 5.1.6 on 2025-03-10 11:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_alter_joinus_options_remove_joinus_user_joinus_email'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoCourseReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('view_date', models.DateTimeField(auto_now_add=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.videocoursereview')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.student')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_video', to='course.videocourse')),
            ],
        ),
    ]
