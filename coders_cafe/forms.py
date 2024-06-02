from .widgets import DatePickerInput
from .models import Booking
from django import forms


class BookingForm(forms.ModelForm):
    """
    Booking class for users to create a booking
    """
    class Meta:
        """
        Specifying the django model, fields, and widgets for user input
        """
        model = Booking
        fields = ['num_seats', 'date', 'start_time']
        time_map = (
            (8, "8am"),
            (9, "9am"),
            (10, "10am"),
            (11, "11am"),
            (12, "12pm"),
            (13, "1pm"),
            (13, "1pm"),
            (14, "2pm"),
            (15, "3pm"),
            (16, "4pm"),
            (17, "5pm"),
            (18, "6pm"),
            (19, "7pm"))
        widgets = {
            'date': forms.widgets.DateInput(attrs = {'type': 'date'}),
            'start_time': forms.Select(choices = time_map),}
