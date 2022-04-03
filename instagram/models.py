from django.utils import timezone
from django.db import models

# import cloudinary
from cloudinary.models import CloudinaryField

class Photos(models.Model):
    '''
    Class that test and handles images
    '''
    title = models.CharField(max_length=20)
    image = CloudinaryField('images/', default='')
    caption = models.CharField(max_length=200)
    likes = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)

    def save_image(self):
        self.save()

    def __str__(self):
        return self.title
