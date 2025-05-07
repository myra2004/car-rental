from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('cars/', include('cars.urls')),
    path('admin/', admin.site.urls),
]
#
static_media_urls = (
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    +
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
=======
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', include('cars.urls')),
]

static_media_urls = (
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        +
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
>>>>>>> 464db674f306f71bb1f1c0192888868881727d73
)

urlpatterns += static_media_urls