# Generated by Django 4.1.13 on 2024-03-04 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0019_paid_course_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paid_course_content',
            name='Which_Course',
        ),
    ]