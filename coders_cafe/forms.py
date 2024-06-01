from .widgets import  DateTimePickerInput
from .models import Booking
from django import forms


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['num_seats', 'start_time']
        widgets = {
            'start_time': DateTimePickerInput(),
        }
