# Generated by Django 4.1.13 on 2024-02-27 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0014_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='particularcourse',
            name='Course_video',
            field=models.CharField(max_length=200),
        ),
    ]
