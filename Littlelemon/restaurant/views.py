from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializers import BookingSerializer, MenuSerializer
from .models import Booking, Menu

def bookings(request):
    return render(request, 'book.html')

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def menu_page(request):
    menu_items = Menu.objects.all()
    return render(request, 'menu.html', {'menu': menu_items})

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class SingleMenuView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        booking_date = self.request.query_params.get('date')
        if booking_date:
            return Booking.objects.filter(reservation_date=booking_date)
        return Booking.objects.all()