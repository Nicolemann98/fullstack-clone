from . import views
from django.urls import path
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='coders_cafe/index.html'), name='index'),
    path('menu/', TemplateView.as_view(template_name='coders_cafe/menu.html'), name='menu'),
    path('cancel/', TemplateView.as_view(template_name='coders_cafe/cancel.html'), name='cancel'),
    path('bookings/', views.BookingList.as_view(), name='bookings'),
    path('manage-booking/<int:booking>', views.manage_booking, name='manage_booking')
]