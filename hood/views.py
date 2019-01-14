from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
import datetime as dt

# Create your views here.

def index(request):
    return render(request, 'index.html')
    
