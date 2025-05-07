from django.contrib import admin
<<<<<<< HEAD
=======
from django.contrib.auth.admin import UserAdmin
>>>>>>> 464db674f306f71bb1f1c0192888868881727d73

from users.models import CustomUser


@admin.register(CustomUser)
<<<<<<< HEAD
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff')
    list_display_links = ('id', 'username', 'email', 'first_name', 'last_name')
    search_fields = ('id', 'username', 'email', 'first_name', 'last_name')

    fieldsets = (
        ('User', {'fields': ('username', 'password', 'email')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'avatar', 'profession', 'bio')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
=======
class CustomUserAdmin(UserAdmin):
    list_display = ("id",  "email", 'username', 'first_name', 'last_name', 'is_staff', 'comments')
    list_display_links = ("id",'username', "email", 'first_name', 'last_name', 'comments')
    search_fields = ('id', "email", 'username', 'first_name', 'last_name')

    fieldsets = (
        ('User', {'fields': ('username', 'password', 'email')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'avatar', 'profession', 'bio', 'comments')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
>>>>>>> 464db674f306f71bb1f1c0192888868881727d73
