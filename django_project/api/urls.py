from django.urls import path
from .views import main , RoomView

urlpatterns = [
    path('', main),
    path('RoomView/' , RoomView.as_view())
]