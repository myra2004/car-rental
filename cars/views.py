<<<<<<< HEAD
from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from django.contrib import messages

from cars.models import Car, Brand
from common.models import ContactMessage
=======
from django.shortcuts import render

from cars.models import Car
>>>>>>> 464db674f306f71bb1f1c0192888868881727d73
from users.models import CustomUser


def index(request):
    cars = Car.objects.all()
    users = CustomUser.objects.filter(
        is_active=True,
<<<<<<< HEAD
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
=======
    )
    comments = CustomUser.objects.filter(
        is_active=True,
        is_staff=False,
        is_superuser=False
    )
    return render(
        request,
        'index1.html',
        context={
            'cars': cars,
            'users': users,
            'comments': comments,
>>>>>>> 464db674f306f71bb1f1c0192888868881727d73
        }
    )
