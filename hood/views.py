from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
import datetime as dt

# Create your views here.

def index(request):
    return render(request, 'index.html')
    
@login_required(login_url='/accounts/login')
def profile(request):
    return render(request,'profile.html')

@login_required(login_url='/accounts/login')
def business(request):
    return render(request, 'business.html')

@login_required(login_url='/accounts/login')
def businesses(request):
    return render(request, 'business.html')

@login_required(login_url='/accounts/login')
def police_stations(request):
    return render(request, 'police_stations.html')
    
@login_required(login_url='/accounts/login')
def health(request):
    return render(request, 'health.html')
