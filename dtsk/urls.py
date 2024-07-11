from django.urls import path, include
from django.contrib import admin

from app import urls

# Default URLS
urlpatterns = [
    path("admin/", admin.site.urls),

    path("", include(urls))
]
