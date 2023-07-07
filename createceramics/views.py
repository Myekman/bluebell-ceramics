from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime, timedelta
from .models import Booking
from .forms import BookingForm
import datetime
from django.contrib import messages


# Create your views here.


def home(request):
    
    return render(request, 'createceramics/home.html')


def about(request, pk):

    return render(request, 'createceramics/about.html')


def services(request):
    
    return render(request, 'createceramics/services.html')


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
            return redirect('mybookings')
        else:
            messages.error(request, "Please enter correct data")
            return render(request, 'booknow.html', {'form': form})
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
    






