# importing user model from django's inbuilt app
from django.contrib.auth.models import User

from django import forms

# importing authentication forms inbuilt authentication
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import UserProfile

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
        fields = UserCreationForm.Meta.fields
        

    username = forms.CharField(
        widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your name'})
    )
    password1 = forms.CharField(
        label= 'Password',
        widget= forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your password'})
    )
    password2 = forms.CharField(
        label= 'Confirm password',
        widget= forms.PasswordInput(attrs={'class':'form-control','placeholder':' Confirm password'})
    )

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['driving_license', 'license_file', 'phone_number', 'address']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['driving_license', 'license_file', 'phone_number', 'address']

    