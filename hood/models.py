from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighbourhood(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    pic = models.ImageField()
    bio = models.TextField()

