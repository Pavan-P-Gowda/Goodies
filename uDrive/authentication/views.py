from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy

# now we r importing inbuilt user regestertation from class
from .forms import CustomLogin, CustomRegister, UserProfileForm, UserEditForm

# importing inbuilt user loginview to inherate and over view the template
from django.contrib.auth.views import LoginView

from django.contrib.auth.decorators import login_required

from .models import UserProfile

# Create your views here.
class UserRegister(CreateView):
    template_name = 'signup.html'
    form_class = CustomRegister
    success_url = reverse_lazy('signin')

class UserLogin(LoginView):
    template_name = 'signin.html'
    form_class = CustomLogin

@login_required
def create_profile(request):
    if hasattr(request.user,'userprofile'):
        return redirect('homepage')
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            print(profile.user.username)
            return redirect('view_profile')
        else:
            print("Form invalid")
    else:
        print("Get request")
        form = UserProfileForm()

    return render(request,'create_profile.html',{'form': form})

@login_required
# def view_profile(request):
#     profile = request.user.userprofile
#     return render(request,'view_profile.html',{'profile',profile})
def view_profile(request):
    try:
        profile = request.user.userprofile
        return render(request, 'authentication/view_profile.html', {'profile': profile})
    except UserProfile.DoesNotExist:
        return redirect('create_profile')

@login_required
def profile_check(request):
    if hasattr(request.user,'userprofile'):
        return redirect('homepage')
    else:
        return redirect('create_profile')

class ProfileEdit(UpdateView):
    model = UserProfile
    context_object_name = 'UserProfile'
    template_name = "profile_edit.html"
    form_class = UserEditForm
    success_url = '/'
