from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import CustomUser


@admin.register(CustomUser)
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
