from django.urls import path

from .views import UserLogin,UserRegister
from . import views

urlpatterns = [
    path('login', UserLogin.as_view(),name = 'signin'),
    path('register', UserRegister.as_view(), name = 'signup'),
    path('profile/create/', views.create_profile, name = 'create_profile'),
    path('profile/view/', views.view_profile, name='view_profile'),
    path('profile/check/', views.profile_check, name='profile_check'),
    path('profile/edit/<int:pk>',views.ProfileEdit.as_view(), name='edit_profile'),
]