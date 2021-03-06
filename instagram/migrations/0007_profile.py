# Generated by Django 4.0.3 on 2022-04-03 15:32

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0006_photos_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=80)),
                ('username', models.CharField(max_length=30)),
                ('profile_image', cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='images/')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
    ]
