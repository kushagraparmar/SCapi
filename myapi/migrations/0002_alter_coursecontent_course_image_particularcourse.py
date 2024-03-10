# Generated by Django 5.0 on 2024-01-26 17:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursecontent',
            name='Course_image',
            field=models.ImageField(unique=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='ParticularCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_video', models.CharField(max_length=100)),
                ('Course_use', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapi.coursecontent')),
            ],
        ),
    ]