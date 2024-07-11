from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.contrib import admin

from app import urls

# Default URLS
urlpatterns = [
    path("admin/", admin.site.urls),

    path("", include(urls))
]


# to show media files in development server
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
