from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime, timedelta
from .models import Booking
# from .forms import BookingForm



# Create your views here.


def home(request):
    
    return render(request, 'createceramics/home.html')


def room(request, pk):

    return render(request, 'createceramics/room.html')

def services(request):
    
    return render(request, 'createceramics/services.html')


def booknow(request):

    return render(request, 'createceramics/booknow.html')



