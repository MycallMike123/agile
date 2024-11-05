from django.shortcuts import render

# Create your views here.
rooms = [
    {'id':1, 'name':'Frontend Developers'},
    {'id':2, 'name':'Backend Developers'},
    {'id':3, 'name':'Full-stack Developers'},
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request):
    return render(request, 'base/room.html')
