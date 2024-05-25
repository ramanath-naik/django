from django.shortcuts import render
from . models import Destination

# Create your views here.

def index(request):

    dest1 = Destination()
    dest1.name = 'mumbai'
    dest1.img = '2.png'

    dest2 = Destination()
    dest2.name = 'Bengaluru'
    dest2.img = '5.png'

    dests = [dest1, dest2]

    return render(request, 'index.html', {'dests': dests}) 