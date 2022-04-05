from django.test import TestCase
from .models import Comments, Profile, Photos, Post

# Create your tests here.

class ProfileTestClass(TestCase):
    '''
    Test class that the profile model
    '''
    def setUp(self):
        self.profile = Profile(bio='more apples')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))


class PostTestClass(TestCase):
    '''
    Test class that handles post model
    '''
    def setUp(self):
        self.post = Post(title='Lawn More')

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))


class CommentsTestClass(TestCase):
    '''
    Test class that handles comments model
    '''
    def setUp(self):
        self.comment = Comments(message='A spirit from Kenya toast to the world')
    def test_instance(self):
        self.assertTrue(isinstance(self.comment, Comments))

class PhotosTestClass(TestCase):
    '''
    Test class that handle comments model 
    '''
    def setUp(self):
        self.photo = Photos(caption='Feels great to be a web developer')

    def test_instance(self):
        self.assertTrue(isinstance(self.photo, Photos))