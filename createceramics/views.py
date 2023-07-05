from django.shortcuts import render
from .models import *



# Create your views here.

rooms = [
    {'id': 1, 'name': 'lets go'},
    {'id': 2, 'name': 'i can do this!'},
    {'id': 3, 'name': 'winner!!'},
]


def home(request):
    # context = {'rooms': rooms}
    return render(request, 'createceramics/home.html')


def room(request, pk):
    # room = None
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i
    # context = {'room': room}
    return render(request, 'createceramics/room.html')

def services(request):
    
    return render(request, 'createceramics/services.html')


def booknow(request):
 
    return render(request, 'createceramics/booknow.html')



