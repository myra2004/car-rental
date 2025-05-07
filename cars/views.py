from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from django.contrib import messages

from cars.models import Car, Brand
from common.models import ContactMessage
from users.models import CustomUser


def index(request):
    cars = Car.objects.all()
    users = CustomUser.objects.filter(
        is_active=True,
        is_superuser=False,
        is_staff=True
    )
    brands = Brand.objects.all()
    return render(
        request=request,
        template_name='index.html',
        context={
            "cars": cars,
            "users": users,
            "brands": brands
        }
    )
