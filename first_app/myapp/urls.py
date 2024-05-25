from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('hello', views.hello, name='hello'),
    path('add', views.add, name='add')
    #   path('',views.test_redis, name='test_redis')
]