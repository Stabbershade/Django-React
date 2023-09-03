from django.urls import path
from .views import main , RoomView , getData

urlpatterns = [
    path('', main),
    path('RoomView/' , RoomView.as_view()),
    path('RoomView2/', getData)
]