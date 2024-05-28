from django.shortcuts import render
from django.views import generic
from .models import Booking

# Create your views here.
class BookingList(generic.ListView):
    queryset = Booking.objects.filter(user_id=2)
    template_name = "coders_cafe/bookings.html"
    paginate_by = 6


class Index(generic.ListView):
    queryset = Booking.objects.filter(user_id=2)
    template_name = "coders_cafe/index.html"
    paginate_by = 6


class Cancel(generic.ListView):
    queryset = Booking.objects.filter(user_id=2)
    template_name = "coders_cafe/cancel.html"
    paginate_by = 6


class Menu(generic.ListView):
    queryset = Booking.objects.filter(user_id=2)
    template_name = "coders_cafe/menu.html"
    paginate_by = 6