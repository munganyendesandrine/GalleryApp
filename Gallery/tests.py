from django.test import TestCase
from .models import Category,Location,Image

# Create your tests here.
class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.Education= Category(name = 'Education')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Education,Category))        

# Create your tests here.
class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.Madagascar= Location(name = 'Madagascar')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Madagascar,Location))      
