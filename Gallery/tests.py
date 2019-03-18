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

class ImageTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.Dove= Image(image_name = 'Dove', image_description ='liked', image_location ='Kigali', image_category='Birds',image='galleryToday/dove.png')
        self.Dove.save_image()

    # Testing  instance
    # def test_instance(self):
    #     self.assertTrue(isinstance(self.Dove,Image))    

    # def tearDown(self):
    #     Image.objects.all().delete()

    

    # # Testing Save Method
    # def test_save_method(self):
    #     self.james.save_editor()
    #     editors = Editor.objects.all()
    #     self.assertTrue(len(editors) > 0)