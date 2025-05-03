from django.urls import path

from cars.views import *


urlpatterns = [
    path('index/', index, name='index'),
]