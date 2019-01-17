from django.test import TestCase
from .views import Neighbourhood,Business,Message,User

# Create your tests here.


class NeighbourhoodTestClass(TestCase):
    #Set up method

    def setUp(self):
        self.kibera = Neighbourhood(hood_name="kibera", hood_location="kibera", occupants=30)

    #Testing Instance

    def test_instance(self):
        self.assertTrue(isinstance(self.kibera, Neighbourhood))

    #Testing the save method

    def test_save_method(self):
        self.kibera.save_hood()
        hoods = Neighbourhood.objects.all()
        self.assertTrue(len(hoods) > 0)


class BusinessTestClass(TestCase):
    #Set up method

    def setUp(self):
        self.business = Business(business_name="fjiqofjoq",biz_person=user.username,hood="kibera",description="serene",email="biz@gmail.com")

    #Testing Instance

    def test_instance(self):
        self.assertTrue(isinstance(self.business, Business))

    #Testing the save method

    def test_save_method(self):
        self.business.save_business()
        businesses = Business.objects.all()
        self.assertTrue(len(businesses) > 0)


