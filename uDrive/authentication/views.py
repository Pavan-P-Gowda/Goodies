from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

# now we r importing inbuilt user regestertation from class
from .froms import CustomLogin, CustomRegister

# importing inbuilt user loginview to inherate and over view the template
from django.contrib.auth.views import LoginView


# Create your views here.
class UserRegister(CreateView):
    template_name = 'signup.html'
    form_class = CustomRegister
    success_url = reverse_lazy('signin')

class UserLogin(LoginView):
    template_name = 'signin.html'
    form_class = CustomLogin

