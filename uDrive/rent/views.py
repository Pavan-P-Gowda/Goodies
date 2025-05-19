from django.shortcuts import render, redirect, get_object_or_404
from .models import RentItem
from mainapp.models import Car
from .forms import RentalDateForm
from django.contrib.auth.decorators import login_required
# Create your views here.
# def addRent(request,car_id):
#     car = get_object_or_404(Car,id=car_id)
#     if request.method == 'POST':
#         form = RentalDateForm(request.Post)
#         if form.is_valid():
#             RentItem.objects.create(
#                 user =request.user,
#                 car = car,
#                 start_date = form.cleaned_data['start_date'],
#                 end_date =form.cleaned_data['end_date']
#             )
#         return redirect('view.cart')
#     else:
#         form = RentalDateForm()
#     return render(request,'addRent.html',{'form':form,'car':car})
@login_required
def rentView(request, car_id):
    items = RentItem.objects.filter(user=request.user)
    # total_price =sum([float(item.total_price())for item in items])
    template = 'rent.html'
    context = {
        'items':items,
        # 'total':total_price
    }
    return render(request,template,context)