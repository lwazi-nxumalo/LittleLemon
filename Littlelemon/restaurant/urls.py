#define URL route for index() view
from django.urls import path
from .views import MenuView , BookingView, index

urlpatterns = [
    path('', index, name='index'),
    path('menu/', MenuView.as_view(), name='menu'),
    path('bookings/', BookingView.as_view(), name='bookings')
]
