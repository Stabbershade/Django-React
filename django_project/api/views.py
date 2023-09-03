from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

from .serializers import RoomSerializer
from .models import Room

#As a class, Return all the room objects from the Room model/database
class RoomView(generics.ListAPIView):
    queryset = Room.objects.all() # Can change the query for more specific items
    serializer_class = RoomSerializer

#Alternatively as a function
@api_view(['GET'])
def getData(request):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer(queryset, many=True)
    return Response(serializer_class.data)

# Create your views here.
def main(request):
    return HttpResponse("Hello")