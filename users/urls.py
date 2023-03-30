from django.urls import  path
from .import views



urlpatterns = [
     path('', views.userlogin, name='userlogin'),
     path('register/', views.register, name='register'),
     path('dashboard/', views.dashboard, name='dashboard'),
     path("logout", views.logout_request, name="logout"),
   
]