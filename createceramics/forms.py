from django import forms



# class BookingForm(forms.ModelForm):
#     """This class generates a form from the Booking model
#     """

#     date = forms.DateField(
#         validators=[MinValueValidator(get_min_date)],
#         widget=DateInput(attrs={'type': 'date', 'min': get_min_date}))

#     class Meta:
#         model = Booking
#         fields = ('name', 'phone', 'email', 'service', 'date', 'time')
#         widgets = {'date': DateInput()}