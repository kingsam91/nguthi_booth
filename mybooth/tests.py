from django.test import TestCase
from .models import Category,Locatoin,Image

# Create your tests here.
class CategoryTestClass(TestCase):

    #Set up method
    def setUp(self):
        self.burger = Category(
            name='Food'
        )

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.burger, Category))

    #Testing save method
    def test_save_method(self):
        self.burger.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)>0)

    def tearDown(self):
        Category.objects.all().delete()