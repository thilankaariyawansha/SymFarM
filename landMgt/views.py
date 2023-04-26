from django.shortcuts import render
from .forms import lands

# Create your views here.
def land(response):
    
    return render(response, "land.html", {})


def addland(response):
    
    if response.user.is_authenticated:
        current_username = response.user.username
        print("----------",current_username)
        adld = lands()
    
        return render(response, "addland.html", { 'addlands':adld })