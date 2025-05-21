from django.shortcuts import render, redirect, get_object_or_404
from .models import RentItem
from mainapp.models import Car
from .forms import RentalDateForm
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.decorators import login_required

@login_required

def rentView(request, car_id):
    item, created_at = RentItem.objects.get_or_create(user=request.user)
    this_car = Car.objects.get(id=car_id)

    if item.car:
        if item.car != this_car:
            return redirect('update_car', car_id)
    else:
        item.car = this_car
        

    error_message = None

    if request.method == 'POST':
        start_date_str = request.POST.get('start_date')
        end_date_str = request.POST.get('end_date')

        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
            today = timezone.now().date()

            if start_date < today:
                error_message = "Start date cannot be in the past."
            elif end_date < start_date:
                error_message = "End date cannot be before start date."
            else:
                item.start_date = start_date
                item.end_date = end_date
                item.save()
                return redirect('homepage')  # Redirect to confirmation/payment

        except ValueError:
            error_message = "Invalid date format."

    item.save()
    total_price = item.total_price
    template = 'rent_confirm.html'

    context = {
        'item': item,
        'total': total_price,
        'error_message': error_message,
        'price_per_day': item.car.price,
        'today': timezone.now().date().isoformat(),  # Format: 'YYYY-MM-DD'
    }
    return render(request, template, context)
# def rentView(request, car_id):
#     item, created_at = RentItem.objects.get_or_create(user=request.user)
#     this_car = Car.objects.get(id=car_id)

#     if item.car:
#         if item.car != this_car:
#             return redirect('update_car', car_id)
#     else:
#         item.car = this_car

#     error_message = None

#     if request.method == 'POST':
#         start_date_str = request.POST.get('start_date')
#         end_date_str = request.POST.get('end_date')

#         try:
#             start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
#             end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
#             today = timezone.now().date()

#             if start_date < today:
#                 error_message = "Start date cannot be in the past."
#             elif end_date < start_date:
#                 error_message = "End date cannot be before start date."
#             else:
#                 item.start_date = start_date
#                 item.end_date = end_date
#                 item.save()
#                 return redirect('homepage')
#         except ValueError:
#             error_message = "Invalid date format."

#     item.save()

#     context = {
#         'item': item,
#         'total': item.total_price,
#         'price_per_day': item.car.price_per_day,
#         'today': timezone.now().date().isoformat(),
#         'error_message': error_message,
#     }

#     return render(request, 'rent_confirm.html', context)

def updateCar(request, car_id):
    template = 'update_car.html'
    rentItem = RentItem.objects.get(user = request.user)
    new_car = Car.objects.get(id = car_id)
    print(new_car.name)
    context = {
        'curr_car' : rentItem ,
        'new_car' : new_car
    }

    if request.method == 'POST':
        rentItem.car = new_car
        rentItem.save()
        return redirect('rentcart', car_id)
        

    return render(request, template, context)