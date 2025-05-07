<<<<<<< HEAD
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from common.models import BaseModel


class Car(BaseModel):
=======
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from common.models import BaseModel

class Car(BaseModel):

>>>>>>> 464db674f306f71bb1f1c0192888868881727d73
    class GearType(models.TextChoices):
        MANUAL = 'Manual'
        AUTO = 'Auto'
        HYBRID = 'Hybrid'

    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    price = models.PositiveIntegerField(null=False, blank=False)
    brand = models.ForeignKey('cars.Brand', on_delete=models.CASCADE, related_name='cars')
    image = models.ImageField(upload_to='cars', null=True, blank=True)
    year = models.PositiveIntegerField(validators=[
        MinValueValidator(1900),
        MaxValueValidator(2025)
    ])
    color = models.CharField(max_length=30)
    gear_type = models.CharField(choices=GearType.choices)
<<<<<<< HEAD
    distance_covered = models.PositiveIntegerField(null=False, blank=False)
=======
    distance_covered = models.PositiveIntegerField(null=False, blank=False )
>>>>>>> 464db674f306f71bb1f1c0192888868881727d73

    def __str__(self):
        return self.name


class Brand(BaseModel):
    name = models.CharField(max_length=100, null=False, blank=False)
    logo = models.ImageField(upload_to='logos', null=True, blank=True)

    def __str__(self):
<<<<<<< HEAD
        return self.name
=======
        return self.name


>>>>>>> 464db674f306f71bb1f1c0192888868881727d73
