# Generated by Django 5.0 on 2024-01-26 18:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_alter_coursecontent_course_image_particularcourse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='particularcourse',
            name='Course_use',
        ),
        migrations.AddField(
            model_name='coursecontent',
            name='Course_use',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='kush', to='myapi.particularcourse'),
            preserve_default=False,
        ),
    ]
