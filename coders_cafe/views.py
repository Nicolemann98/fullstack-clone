from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Booking
from .forms import BookingForm

class BookingList(generic.ListView):
    model = Booking
    template_name = "coders_cafe/bookings.html"
    context_object_name = 'all_bookings_by_user'

    def get_queryset(self):
        if (not self.request.user.is_authenticated):
            return Booking.objects.none()
            
        return Booking.objects.filter(user=self.request.user)


def manage_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)

    if (booking.user != request.user):
        booking = Booking.objects.none()

    if request.method == "POST":
        booking_form = BookingForm(data=request.POST, instance=booking)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.save()
            return HttpResponseRedirect("success")
    else:
        booking_form = BookingForm(instance=booking)
    
    return render(
        request,
        "coders_cafe/manage_booking.html",
        {
            "booking": booking,
            "booking_form": booking_form,
        },
    )


def create_booking(request):
    if request.method == "POST":
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            setattr(booking, "user", request.user)
            booking.save()
            return HttpResponseRedirect("success")
    else:
        booking_form = BookingForm()

    return render(
        request,
        "coders_cafe/create_booking.html",
        {
            "booking_form": booking_form,
        },
    )