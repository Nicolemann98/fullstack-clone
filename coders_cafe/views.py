from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Booking
from .forms import BookingForm
from datetime import datetime


class BookingList(generic.ListView):
    """
    Returns all bookings in :model:`coders_cafe.Booking`
    that elong to the logged in user and that are either
    for today or any date in the future and displays them 
    """ 
    model = Booking
    template_name = "coders_cafe/bookings.html"
    context_object_name = 'all_bookings_by_user'
    paginate_by: 6

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Booking.objects.none()
            
        if self.request.user.is_staff:
            return Booking.objects.filter(date__gte=datetime.today())
        else:
            return Booking.objects.filter(user=self.request.user,
            date__gte=datetime.today())


def manage_booking(request, booking_id):
    """
    Displays an individual :model:`coders_cafe.Booking`
    and allows the user to submit a post request to edit
    that booking
    """
    booking = get_object_or_404(Booking, pk=booking_id)

    if (booking.user != request.user):
        booking = Booking.objects.none()

    if request.method == "POST":
        booking_form = BookingForm(data=request.POST, instance=booking)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)

            if not validate_booking(booking, request):
                return render(
                    request,
                    "coders_cafe/manage_booking.html",
                    {
                        "booking": booking,
                        "booking_form": booking_form,
                    },
                )

            booking.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Booking successfully edited'
            )
            return HttpResponseRedirect(reverse("bookings"))
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
    """
    Create an individual booking
    """
    if request.method == "POST":
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            setattr(booking, "user", request.user)

            if not validate_booking(booking, request):
                return render(
                    request,
                    "coders_cafe/create_booking.html",
                    {
                        "booking_form": booking_form,
                    },
                )
            
            else:
                booking.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    'Booking successfully created'
                )
                return HttpResponseRedirect(reverse("bookings"))
        else:
            messages.add_message(request, messages.ERROR, "Booking not valid")

    else:
        booking_form = BookingForm()

    return render(
        request,
        "coders_cafe/create_booking.html",
        {
            "booking_form": booking_form,
        },
    )


def delete_booking(request, booking_id):
    """
    Delete an individual booking
    """
    booking = get_object_or_404(Booking, pk=booking_id)

    if (booking.user == request.user):
        booking.delete()
        messages.add_message(
            request, messages.SUCCESS,
            'Booking successfully deleted'
        )
    else:
        messages.add_message(
            request, messages.ERROR,
            'You can only delete your own booking'
        )

    return HttpResponseRedirect(reverse("bookings"))
        

def validate_booking(booking, request):
    """
    Perform validation on the user's submitted booking
    Including ensuring the booking time/date is in the future
    and that the cafe does no exceed their total number of seats
    """
    if has_booking_exceeded_capacity(booking):        
        messages.add_message(request, messages.ERROR, "Booking unsuccessful. Not enough seats available")
        return False

    if is_chosen_datetime_in_past(booking):        
        messages.add_message(request, messages.ERROR, "Booking unsuccessful. Booking date/time is in the past")
        return False
    
    return True


def has_booking_exceeded_capacity(booking):
    """
    Ensures the incoming booking does not make the cafe
    exceed their total number of seats
    """
    capacity = 20

    all_overlapping_bookings = Booking.objects.filter(
        date = booking.date,
        start_time = booking.start_time).exclude(id=booking.id)
    total_seats_reserved = booking.num_seats
    for other_booking in all_overlapping_bookings:
        total_seats_reserved += other_booking.num_seats
    
    if total_seats_reserved > capacity:
        return True
    else:
        return False


def is_chosen_datetime_in_past(booking):
    """
    Ensures the incoming booking is in the future
    """
    if booking.date < datetime.today().date():
        return True
    elif booking.date == datetime.today().date() and booking.start_time < datetime.now().hour:
        return True