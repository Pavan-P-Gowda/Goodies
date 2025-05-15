# importing user model from django's inbuilt app
from django.contrib.auth.models import User

from django import forms

# importing authentication forms inbuilt authentication
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class CustomLogin(AuthenticationForm):
    username = forms.CharField(
        widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your name'})
    )
    password = forms.CharField(
        widget= forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your password'})
    )

class CustomRegister(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','password','confirmpassword')

    username = forms.CharField(
        label= 'Paaword',
        widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your name'})
    )
    password = forms.CharField(
        label= 'Paaword',
        widget= forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your password'})
    )
    confirmpassword = forms.CharField(
        label= 'Confirm password',
        widget= forms.PasswordInput(attrs={'class':'form-control','placeholder':' Confirm password'})
    )

    