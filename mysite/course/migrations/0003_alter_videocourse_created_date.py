# Generated by Django 5.1.6 on 2025-03-13 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videocourse',
            name='created_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
