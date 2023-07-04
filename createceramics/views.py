from django.shortcuts import render

# Create your views here.

rooms = [
    {'id': 1, 'name': 'lets go'},
    {'id': 2, 'name': 'i can do this!'},
    {'id': 3, 'name': 'winner!!'},
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'createceramics/home.html', context)

def room(request, pk):
    return render(request, 'createceramics/room.html')