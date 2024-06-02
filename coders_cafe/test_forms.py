from django.test import TestCase
from .forms import BookingForm
import datetime


class TestBookingForm(TestCase):


    def test_form_is_valid(self):
        booking_form = BookingForm({"num_seats": 2,
        "date": datetime.date(2024,1,1), "start_time":8})
        self.assertTrue(booking_form.is_valid(),
        "The form is not valid")


    def test_start_time_min_value(self):
        booking_form = BookingForm({"num_seats": 2,
        "date": datetime.date(2024,1,1), "start_time":7})
        self.assertFalse(booking_form.is_valid(),
        "The form should be invalid when start_time is before opening time")


    def test_start_time_max_value_inside_range(self):
        booking_form = BookingForm({"num_seats": 2,
        "date": datetime.date(2024,1,1), "start_time":19})
        self.assertTrue(booking_form.is_valid(),
        "The form should be valid with start_time just before closing time")


    def test_start_time_max_value_outside_range(self):
        booking_form = BookingForm({"num_seats": 2,
        "date": datetime.date(2024,1,1), "start_time":20})
        self.assertFalse(booking_form.is_valid(),
        "The form should be invalid with start_time just after closing time")


    def test_num_seats_required(self):
        booking_form = BookingForm({"num_seats": None,
        "date": datetime.date(2024,1,1), "start_time":20})
        self.assertFalse(booking_form.is_valid(),
        "The form should be invalid with num_seats not provided")


    def test_date_required(self):
        booking_form = BookingForm({"num_seats": 2,
        "date": None, "start_time":20})
        self.assertFalse(booking_form.is_valid(),
        "The form should be invalid with date not provided")


    def test_start_time_required(self):
        booking_form = BookingForm({"num_seats": 2,
        "date": datetime.date(2024,1,1), "start_time":None})
        self.assertFalse(booking_form.is_valid(),
        "The form should be invalid with start_time not provided")
