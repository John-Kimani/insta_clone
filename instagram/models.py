from email.policy import default
from django.db import models

# import cloudinary
from cloudinary.models import CloudinaryField

class Photos(models.Model):
    '''
    Class that test and handles images
    '''
    title = models.CharField(max_length=20)
    image = CloudinaryField('images/', default='')

    def save_image(self):
        self.save()

    def __str__(self):
        return self.title
