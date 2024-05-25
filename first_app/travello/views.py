from django.shortcuts import render
from . models import Destination

# Create your views here.

def index(request):
    dest1 = Destination()
    dest1.name = 'mumbai'
    # dest1.img = '2.png'
    return render(request, 'index.html', {'dest1': dest1}) 