from django.contrib import admin

<<<<<<< HEAD
from common.models import MediaFile, ContactMessage

@admin.register(MediaFile)
class MediaFileAdmin(admin.ModelAdmin):
    list_display = ('file', 'car')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'subject')
    list_display_links = ('id', 'name', 'email')
    search_fields = ('id', 'name', 'email', 'subject')
    list_filter = ('subject',)
=======
from common.models import MediaFile


@admin.register(MediaFile)
class MediaFileAdmin(admin.ModelAdmin):
    list_display = ("file", 'car')
>>>>>>> 464db674f306f71bb1f1c0192888868881727d73
