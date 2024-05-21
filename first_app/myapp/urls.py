from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name='home')
    #   path('',views.test_redis, name='test_redis')
]