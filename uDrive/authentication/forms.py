# importing user model from django's inbuilt app
from django.contrib.auth.models import User

from django import forms

# importing authentication forms inbuilt authentication
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import UserProfile
from django.forms import Textarea

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
        widgets = {
            'address': Textarea(attrs={
                'rows': 4,  # height
                'cols': 40,  # width
                'style': 'width: 240px; height: 250px;',  # optional inline CSS
            }),
        }

    def clean_phone_number(self):
        """Validate that phone number is exactly 10 digits."""
        phone_number = self.cleaned_data.get("phone_number")
        if not phone_number.isdigit() or len(phone_number) != 10:
            raise forms.ValidationError("Phone number must be exactly 10 digits.")
        return phone_number

class UserEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['driving_license', 'license_file', 'phone_number', 'address']
        widgets = {
            'address': Textarea(attrs={
                'rows': 4,  # height
                'cols': 40,  # width
                'style': 'width: 240px; height: 250px;',  # optional inline CSS
            }),
        }
    def clean_phone_number(self):
        """Validate that phone number is exactly 10 digits."""
        phone_number = self.cleaned_data.get("phone_number")
        if not phone_number.isdigit() or len(phone_number) != 10:
            raise forms.ValidationError("Phone number must be exactly 10 digits.")
        return phone_number

