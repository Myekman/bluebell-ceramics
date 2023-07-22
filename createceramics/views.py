from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime, timedelta
from .models import Booking
from .forms import BookingForm
import datetime
from django.contrib import messages


# Create your views here.


def home(request):
    return render(request, 'createceramics/home.html')


def about(request):

    return render(request, 'createceramics/about.html')


def booknow(request):
    """The view for the booking page. If user is logged in it renders the
    booknow.html, otherwise it redirects user to the login page or signup page.
    """
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking_form = form.save(commit=False)
            booking_form.user = request.user
            booking_form.save()
            messages.success(request, 'Booking is confirmed')
            return redirect('mybookings')
        else:
            messages.add_message(request, messages.WARNING, 'the time is not avalible, please pick another one')
            # messages.error(request, 'the time is not avalible, please pick another one')
            return render(request, 'createceramics/booknow.html', {'form': form})
    form = BookingForm()
    return render(request, 'createceramics/booknow.html', {'form': form})


def mybookings(request):
    """The view that renders the mybookings.html which shows all
    current booking by the user. Checks if user is logged in
    otherwise it redirects to the signup page.
    """
    if request.user.is_authenticated:
        bookings = Booking.objects.filter(user=request.user)
        context = {
           'bookings': bookings
        }
        return render(request, 'createceramics/mybookings.html', context)
    else:
        return redirect('../accounts/signup')


def edit_booking(request, booking_id):
    """The view that renders the change_booking page where the user can
    update a current booking.
    """
    record = get_object_or_404(Booking, id=booking_id)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, 'You succesfully updated your booking.')
            return redirect('mybookings')
        else:
            return render(request, 'createceramics/edit_booking.html', {'form': form})
    form = BookingForm(instance=record)
    context = {'form': form, 'record': record}
    return render(request, 'createceramics/edit_booking.html', context)


def delete_booking(request, booking_id):
    """
    Function enables user to delete a booking record
    """
    booking = Booking.objects.get(pk=booking_id)
    booking.delete()
    messages.success(request, 'Booking has been deleted')
    return redirect('mybookings')






