from . import views
from django.urls import path

urlpatterns = [
    path('bookings/', views.BookingList.as_view(), name='bookings'),
    path('', views.Index.as_view(), name='index'),
    path('menu/', views.Menu.as_view(), name='menu'),
    path('cancel/', views.Cancel.as_view(), name='cancel'),
]