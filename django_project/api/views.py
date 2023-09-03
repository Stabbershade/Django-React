from django.shortcuts import render
from django.http import HttpResponse
from .serializers import RoomSerializer
from .models import Room
 
from rest_framework import generics

#Return all the room objects from the Room model/database
class RoomView(generics.ListAPIView):
    queryset = Room.objects.all() # Can change the query for more specific items
    serializer_class = RoomSerializer

# Create your views here.
def main(request):
    return HttpResponse("Hello")