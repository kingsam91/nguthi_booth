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


class LocatoinTestClass(TestCase):

    def setUp(self):
        self.location = Locatoin(
            name='Mombasa'
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Locatoin))

    def test_save_method(self):
        self.location.save_location()
        locations = Locatoin.objects.all()
        self.assertTrue(len(locations)>0)