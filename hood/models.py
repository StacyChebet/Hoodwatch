from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Business(models.Model):
    # admin = models.ForeignKey()
    hood_name = models.CharField(max_length = 40)
    hood_location = models.CharField(max_length=40)
    occupants = models.IntegerField(blank=True)

    @classmethod
    def get_all_businesses(self):
        businesses = Business.objects.all()
        return businesses

