from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighbourhood(models.Model):
    # admin = models.ForeignKey()
    hood_name = models.CharField(max_length = 40)
    hood_location = models.CharField(max_length=40)
    occupants = models.IntegerField(blank=True)

    @classmethod
    def get_all_businesses(self):
        businesses = Business.objects.all()
        return businesses

class User(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    user_id = models.CharField(primary_key=True, max_length=10)
    hood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    email = models.EmailField(max_length=60)

    @classmethod
    def get_all_users(self):
        users = User.objects.all()
        return users




