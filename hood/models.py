from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighbourhood(models.Model):

    NEIGHBOURHOOD_CHOICES = (
        ('Kibera', 'KIBERA'),
        ('Dandora', 'DANDORA'),
    )
    hood_name = models.CharField(max_length = 40)
    hood_location = models.CharField(max_length=40, choices=NEIGHBOURHOOD_CHOICES)
    occupants = models.IntegerField(blank=True, null=True)

    @classmethod
    def get_all_neighbourhoods(self):
        neighbourhoods = Neighbourhood.objects.all()
        return neighbourhoods

    def save_hood(self):
        self.save()

    

class Profile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    user_id = models.CharField(primary_key=True, max_length=10)
    hood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    email = models.EmailField(max_length=60)

    @classmethod
    def get_all_users(cls):
        users = cls.objects.all()
        return users

    def save_user(self):
        self.save()


class Business(models.Model):
    business_name = models.CharField(max_length=200)
    biz_person = models.ForeignKey(User, on_delete=models.CASCADE)
    hood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    email = models.EmailField()

    @classmethod
    def get_all_businesses(self):
        businesses = Business.objects.all()
        return businesses

    @classmethod
    def search_by_business_name(cls,search_term):
        businesses = cls.objects.filter(title__icontains = search_term)
        return businesses
    
    def save_business(self):
        self.save()

class Hospital(models.Model):
    hosp_name = models.CharField(max_length=200)
    location = models.CharField(max_length=60)
    email = models.EmailField()
    phone = models.CharField(max_length = 10)

    def __str__(self):
        return self.hosp_name
    
    @classmethod
    def get_hospitals(self):
        hospitals = Hospital.objects.all()
        return hospitals
    
    def save_hospital(self):
        self.save()

class Message(models.Model):
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.TextField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    comments = models.TextField()

    def __str__(self):
        return self.poster

    @classmethod
    def get_messages(self):
        messages = Message.objects.all()
        return messages

    def save_message(self):
        self.save()

class Station(models.Model):
    location = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    email = models.EmailField()

    @classmethod
    def get_stations(self):
        stations = Station.objects.all()
        return stations

    def save_station(self):
        self.save()



    



