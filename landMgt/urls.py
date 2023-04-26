from django.urls import  path
from .import views



urlpatterns = [
     path('land', views.land, name='land'),
     path('addland', views.addland, name='addland'),
     
     
     
]