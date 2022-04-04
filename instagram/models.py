from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models

# import cloudinary
from cloudinary.models import CloudinaryField

class Comments(models.Model):
    '''
    Class that handles user comments
    '''
    message = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message


class Profile(models.Model):
    '''
    Class that handles user profile
    '''
    bio = models.CharField(max_length=80)
    username = models.CharField(max_length=30)
    profile_image = CloudinaryField('images/', default='')
    name = models.CharField(max_length=40)

    @classmethod
    def display_profile(cls):
        '''
        Function that displays user profile
        '''
        profile = cls.objects.all()
        return profile


    def __str__(self):
        return self.username


class Photos(models.Model):
    '''
    Class that test and handles images
    '''
    title = models.CharField(max_length=20)
    image = CloudinaryField('images/', default='')
    caption = models.CharField(max_length=200)
    likes = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)
    comments = models.ForeignKey(Comments, on_delete=models.CASCADE)

    @classmethod
    def display_all(cls):
        '''
        Function that dislays post information
        '''
        caption = cls.objects.all()
        return caption

    def save_post(self):
        self.save()

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=20)
    image = CloudinaryField('images/', default='')
    caption = models.CharField(max_length=200)
    likes = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)
    comments = models.ForeignKey(Comments, on_delete=models.CASCADE)

    @classmethod
    def display_posts(cls):
        posts = cls.objects.all()
        return posts

    def __str__(self):
        return self.title