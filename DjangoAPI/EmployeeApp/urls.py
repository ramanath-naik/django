
from django.urls import path, re_path
from EmployeeApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('home', views.home),
    path('calculator', views.calculator),
    path('api/departments/', views.departmentApi),
    path('api/departments/<int:id>/', views.departmentApi),
    path('api/employees/', views.employeeApi),
    path('api/employees/<int:id>/', views.employeeApi),
    path('api/savefile/', views.SaveFile),
    re_path(r'^.*$', views.index),  # Catch-all for the front-end
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
