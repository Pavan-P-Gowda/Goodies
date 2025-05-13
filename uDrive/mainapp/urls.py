from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='homepage'),
    path('about',views.about,name= 'aboutpage'),
    path('contact',views.contact,name= 'contactpage'),
    path('car/<int:pk>',views.CarDetails.as_view(), name='car_detail'),
    path('car/add',views.AddCar.as_view(), name='add_car'),
    path('car/edit/<int:pk>',views.CarEdit.as_view(), name = 'car_edit'),
    path('car/delete/<int:pk>', views.CarDelete.as_view(),name = 'delete_car')
]