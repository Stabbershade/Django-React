from django.urls import path , include
from .views import index

urlpatterns = [
    path('', index),
     path('Signup/', index),
    path('Sample1/', index),
    path('Sample2/', index),
]