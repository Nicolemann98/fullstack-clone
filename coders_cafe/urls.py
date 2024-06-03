from . import views
from django.urls import path
from django.views.generic.base import TemplateView

urlpatterns = [
    path('',
         TemplateView.as_view(template_name='coders_cafe/index.html'),
         name='index'),
    path('menu/',
         TemplateView.as_view(template_name='coders_cafe/menu.html'),
         name='menu'),
    path('account/',
         TemplateView.as_view(template_name='coders_cafe/account.html'),
         name='account'),
    path('bookings/',
         views.BookingList.as_view(),
         name='bookings'),
    path('create-booking/',
         views.create_booking,
         name='create_booking'),
    path('bookings/manage-booking/<int:booking_id>',
         views.manage_booking,
         name='manage_booking'),
    path('bookings/delete-booking/<int:booking_id>',
         views.delete_booking
         name='delete_booking'),
]
