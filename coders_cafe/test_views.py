from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import BookingForm
from .models import Booking
import datetime

class TestBookingViews(TestCase):


    def setUp(self):
        self.user = User.objects.create_user(
            username = "myUsername",
            password = "myPassword",
            email = "test@test.com")
        self.tomorrow = datetime.date.today() + datetime.timedelta(days = 1)
        self.booking = Booking(id = 1, user = self.user, date = self.tomorrow,
        start_time = 8, num_seats = 2)
        self.booking.save()


    def test_manage_booking_page_get(self):
        """Test for opening manage booking page"""
        self.client.login(username = "myUsername", password = "myPassword",)
        response = self.client.get(reverse('manage_booking', args = [1]))

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Num seats", response.content)
        self.assertIn(b"Date", response.content)
        self.assertIn(b"Start time", response.content)
        self.assertIsInstance(response.context['booking_form'], BookingForm)


    def test_manage_booking_page_get_throws_404_when_no_booking(self):
        """TEst for opening manage booking page without valid booking"""
        self.client.login(username = "myUsername", password = "myPassword",)
        response = self.client.get(reverse('manage_booking', args = [2]))

        self.assertEqual(response.status_code, 404)
        self.assertNotIn(b"Num seats", response.content)
        self.assertNotIn(b"Date", response.content)
        self.assertNotIn(b"Start time", response.content)


    def test_create_booking_page_get(self):
        """Test for opening create booking page"""
        self.client.login(username = "myUsername",
        password = "myPassword",)
        response = self.client.get(reverse('create_booking'))

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Num seats", response.content)
        self.assertIn(b"Date", response.content)
        self.assertIn(b"Start time", response.content)
        self.assertIsInstance(response.context['booking_form'], BookingForm)


    def test_successful_booking_creation(self):
        """Test for creating new booking"""
        self.client.login(username = "myUsername", password = "myPassword",)
        booking_data = {"num_seats": 2, "date": self.tomorrow,
        "start_time": 9}
        response = self.client.post(reverse('create_booking'), booking_data)
        self.assertEqual(response.status_code, 302)


    def test_unsuccessful_booking_creation(self):
        """Test for unsuccessfully creating new booking"""
        self.client.login(username = "myUsername", password = "myPassword",)
        booking_data = {"num_seats": 2, "date": self.tomorrow,
            "start_time": 21}
        response = self.client.post(reverse('create_booking'),
        data = booking_data)
        self.assertNotEqual(response.status_code, 302)
