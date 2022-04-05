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
