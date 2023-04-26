from django.shortcuts import render
from django.contrib.auth import logout
from .forms import Registratoin, login_from
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Create your views here.
def register(response):
    if response.method == 'POST':
        form = Registratoin(response.POST)
        if form.is_valid():
            form.save()
        form.cleaned_data
        messages.success(response, 'Registerd Sucussfully ')
        form = Registratoin()
            
            
    else:
        form = Registratoin()
        
    return render(response, 'register.html', {"form":form})




def userlogin(response):
    if response.method == 'POST':
        username = response.POST['username']
        password = response.POST['password']
       
        user = authenticate(response, username=username, password=password)
        if user is not None:
            login(response, user)
            return redirect('dashboard')  # redirect to your home page
        else:
            form = login_from()
            error_message = 'Invalid login credentials. Please try again.'
    else:
        form = login_from()
        error_message = ''
    return render(response, 'home.html', {'form': form , 'error_message': error_message})


def dashboard(response):
    username = response.user.username
    return render(response,'dashboard.html', {'username':username} )



def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("userlogin")

def user_verify(response):
    if response.method == 'POST':
        username = response.POST['username']
        password = response.POST['password']
       
        user = authenticate(response, username=username, password=password)
        if user is not None:
            uvfd = "Yes"
            unam = username
        else:
            uvfd = "No"
            unam = ''
    else:
        uvfd = "No"
        unam = ''
        
    return uvfd, unam


def reset_pwd(response):
  
        
    return render(response,'pwd_reset.html', {} )

    
