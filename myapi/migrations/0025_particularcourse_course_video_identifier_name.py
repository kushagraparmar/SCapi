# Generated by Django 4.1.13 on 2024-03-07 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0024_register_course_purchased'),
    ]

    operations = [
        migrations.AddField(
            model_name='particularcourse',
            name='Course_video_identifier_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
