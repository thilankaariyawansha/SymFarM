from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Registratoin(UserCreationForm):
    # add required fields other than parental fiels (username, password, etc)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length = 100)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class login_from(forms.Form):
    # add required fields other than parental fiels (username, password, etc)
    username = forms.CharField(label= 'User Name / පරිශීලක නාමය')
    password = forms.CharField(label= 'Password / මුර පදය ', widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = "__all__"