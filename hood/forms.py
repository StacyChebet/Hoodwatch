from django import forms
from .models import Neighbourhood,Business,Profile,Message,Station

class AddBusiness(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['biz_person', 'hood']

class AddMessage(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ['poster', 'hood', 'pub_date', 'comments']

class AddHood(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        exclude = ['hood_name', 'occupants']


