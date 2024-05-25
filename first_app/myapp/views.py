from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.cache import cache

from .models import *

# Create your views here.

# def home(request):
#     objs = Fruits.objects.all()

#     payload = []
#     for obj in objs:
#         payload.append(obj.fruit_name)

#     return JsonResponse({'status' : 200, 'db': 'sqlite', 'data': payload});


def home(request):
    payload = []
    db = None

    if cache.get('fruits'):
        payload = cache.get('fruits')
        db = 'redis'
        print(cache.ttl("fruits"))
    else:
        objs = Fruits.objects.all()
        for obj in objs:
            payload.append(obj.fruit_name)
        db = 'sqlite'

        cache.set('fruits',payload, timeout=10)

    return JsonResponse({'status' : 200, 'db': db, 'data': payload});

# def test_redis(request):
#     try:
#         # Attempt to set and get a value in the Redis cache
#         cache.set('test_key', 'test_value', timeout=30)
#         value = cache.get('test_key')
#         if value == 'test_value':
#             return JsonResponse({'status': 'success', 'message': 'Redis is working!'})
#         else:
#             return JsonResponse({'status': 'error', 'message': 'Redis is not returning the correct value.'})
#     except Exception as e:
#         return JsonResponse({'status': 'error', 'message': str(e)})


def hello(request):
    return render(request, 'home.html',{'name':'naveen'})  #to pass dynamic value

def add(request):
    val1= int(request.POST['num1'])  #we are not sending data in url. (i.e importance of post method)
    val2= int(request.POST['num2'])
    res = val1+val2
    return render(request, "result.html", {'result':res})