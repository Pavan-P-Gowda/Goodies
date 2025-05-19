from django.urls import path 
from . import views
urlpatterns =[
    # path('car/<int:car_id>/add/', views.addRent, name='addrent'),
    path('rent/<int:car_id>/', views.rentView, name='rentcart'),
]