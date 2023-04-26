from django.urls import  path
from .import views



urlpatterns = [
     path('machine', views.machine, name='machine'),
     path('addMachine', views.addMachine, name='addMachine'),
     
]