from django.urls import path 
from . import views
urlpatterns =[
    # path('car/<int:car_id>/add/', views.addRent, name='addrent'),
    path('add/<int:car_id>/', views.rentView, name='rentcart'),
    path('update/<int:car_id>', views.updateCar, name = 'update_car')
]