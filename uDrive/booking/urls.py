from django.urls import path
from . import views
app_name = 'booking'

urlpatterns = [
    path('create/', views.create_booking, name='create_booking'),
    path('success/<int:pk>/', views.booking_success, name='success_page'),
    path('history/', views.booking_history, name='history'),
]