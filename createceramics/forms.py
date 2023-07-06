from django import forms
from .models import Booking

class DateInput(forms.DateInput):
    """This class provides a widget that the user can
    click on. It cretes a better UX when choosing the date
    for the booking.
    """
    input_type = 'date'


