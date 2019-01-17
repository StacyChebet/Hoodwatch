from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
import datetime as dt
from django.contrib.auth.models import User
from .models import Neighbourhood,Profile,Business,Hospital,Message,Station
from .forms import AddBusiness,AddMessage,AddHood

# Create your views here.

def index(request):
    businesses = Business.objects.all()
    messages = Message.objects.all()
    return render(request, 'index.html', {"businesses":businesses, "messages":messages})
    
@login_required(login_url='/accounts/login')
def profile(request):
    businesses = Business.objects.filter(biz_person_id=request.user.id)
    current_user = User.objects.get(username=request.user)
    if request.method == 'POST':
        form = AddHood(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.save()
        return redirect('profile')
    else:
        form = AddHood()
    return render(request, 'profile.html', {"form": form, "businesses":businesses})

@login_required(login_url='/accounts/login')
def business(request):
    businesses = Business.objects.all()
    return render(request, 'business.html', {"businesses":businesses})

@login_required(login_url='/accounts/login')
def police_stations(request):
    stations = Station.objects.all()
    return render(request, 'police_stations.html', {"stations":stations})
    
@login_required(login_url='/accounts/login')
def health(request):
    hospitals = Hospital.objects.all()
    return render(request, 'health.html', {"hospitals":hospitals})

@login_required(login_url='/accounts/login')
def add_business(request):
    current_user = User.objects.get(username = request.user)
    if request.method == 'POST':
        form = AddBusiness(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.biz_person = current_user
            business.save()
        return redirect('index')

    else:
        form = AddBusiness()
    return render(request, 'add_business.html', {"form": form})


@login_required(login_url='/accounts/login')
def add_post(request):
    current_user = User.objects.get(username = request.user)
    if request.method == 'POST':
        form = AddMessage(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.poster = current_user
            message.save()
        return redirect('index')
    else:
        form = AddMessage()
    return render(request, 'add_post.html', {"form":form})


@login_required(login_url='/accounts/login')
def add_hood(request):
    current_user = User.objects.get(username=request.user)
    if request.method == 'POST':
        form = AddHood(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.save()
        return redirect('profile')
    else:
        form = AddHood()
    return render (request, 'profile.html', {"form":form})

@login_required(login_url='/accounts/login')
def search_results(request):
    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_businesses = Business.search_by_business_name(search_term)

        return render(request, 'search_results.html', {"businesses": searched_businesses})

    else:
        message = "You haven't searched for any article"
        return render(request, 'search_results.html', {"message": message})
    
