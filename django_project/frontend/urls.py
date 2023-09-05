from django.urls import path , include
from .views import index

urlpatterns = [
    path('', index),
    path('Sample1/', index),
    path('Sample2/', index),
]