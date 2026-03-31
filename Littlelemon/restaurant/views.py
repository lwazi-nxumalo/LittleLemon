from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import  generics , viewsets
from rest_framework.views import APIView
from .serializers import BookingSerializer, MenuSerializer
from rest_framework.response import Response
from .models import Booking, Menu

# Create your views here.
def index(request):
    return render(request, 'index.html' , {})

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuView(generics.RetrieveUpdateAPIView , generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer