from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Booking
# from .forms import BookingForm

# Create your views here.
class BookingList(generic.ListView):
    model = Booking
    template_name = "coders_cafe/bookings.html"
    context_object_name = 'all_bookings_by_user'

    def get_queryset(self):
        if (not self.request.user.is_authenticated):
            return Booking.objects.none()
            
        return Booking.objects.filter(user=self.request.user)


def manage_booking(request, booking):
    try:
        booking = Booking.objects.get(pk=booking)
    except Booking.DoesNotExist:
        booking = None
    # booking_form = BookingForm()

    return render(
        request,
        "coders_cafe/manage_booking.html",
        {
            "booking": booking,
            # "booking_form": booking_form,
        },
    )