# Generated by Django 4.1.13 on 2024-03-07 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0025_particularcourse_course_video_identifier_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='paid_course_content',
            name='Selected_Student',
            field=models.ForeignKey(blank=True, default=36, on_delete=django.db.models.deletion.CASCADE, related_name='Selected', to='myapi.register'),
            preserve_default=False,
        ),
    ]
