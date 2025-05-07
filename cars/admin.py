from django.contrib import admin

from cars.models import Car, Brand


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ('name', 'price', 'year', 'color', 'gear_type', 'distance_covered')
    list_filter = ('brand', 'gear_type')
    search_fields = ('name', 'description')
=======
    list_display = ("id", "name", "price", 'color', "gear_type", 'distance_covered')
    list_filter = ('brand', "gear_type")
    search_fields = ("name", 'description')
>>>>>>> 464db674f306f71bb1f1c0192888868881727d73


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ('name', 'logo')
    search_fields = ('name', 'description')
=======
    list_display = ("name", 'logo')
    search_fields = ("name", 'description')


>>>>>>> 464db674f306f71bb1f1c0192888868881727d73
