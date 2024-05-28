from django.shortcuts import render, get_object_or_404
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


def booking_detail(request, booking_id):
    print("The booking id is" + booking_id)

    """
    Display an individual :model:`coders_cafe.Booking`.

    **Context**

    ``booking``
        An instance of :model:`coders_cafe.Booking`.

    **Template:**

    :template:`coders_cafe/booking_detail.html`
    """

    queryset = Booking.objects.filter(id=booking_id)
    booking = get_object_or_404(queryset)

    return render(
        request,
        "coders_cafe/booking_detail.html",
        {"booking": booking},
    )