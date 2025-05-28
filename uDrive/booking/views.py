from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Booking, BookingHistory
from mainapp.models import Car
from datetime import datetime

# Create your views here.
@login_required
def create_booking(request):
    car_id = request.GET.get('car_id')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    total_cost = request.GET.get('total_cost')

    car = Car.objects.get(id=car_id)

    booking = Booking.objects.create(
        user=request.user,
        car=car,
        start_date=start_date,
        end_date=end_date,
        total_cost=total_cost
    )

    # Instead of direct redirect, show success page with "Pay Now" link
    return redirect('booking:success_page', booking_id=booking.id)

def booking_success(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    return render(request, 'booking/success.html', {'booking': booking})

@login_required
def booking_history(request):
    histories = BookingHistory.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'booking/history.html', {'histories': histories})

