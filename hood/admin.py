from django.contrib import admin
from .models import Neighbourhood,Profile,Business,Hospital,Message,Station

# Register your models here.
admin.site.register(Neighbourhood)
admin.site.register(Profile)
admin.site.register(Business)
admin.site.register(Hospital)
admin.site.register(Message)
admin.site.register(Station)
