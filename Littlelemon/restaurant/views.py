from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import APIView
from rest_framework.response import Response
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer
# Create your views here.
def index(request):
    return render(request, 'index.html' , {})

class BookingView(APIView):
    def get(self, request):
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)
    
class MenuView(APIView):
    def post(self, request):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status" : "success" , "data" : serializer.data}, status=201)
        return Response({"status" : "error" , "data" : serializer.errors}, status=400)