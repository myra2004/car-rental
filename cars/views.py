from django.shortcuts import render

from cars.models import Car
from users.models import CustomUser


def index(request):
    cars = Car.objects.all()
    users = CustomUser.objects.filter(
        is_active=True,
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
        }
    )
