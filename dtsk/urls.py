from django.urls import path, include
from django.contrib import admin

# Default URLS
urlpatterns = [
    path("admin/", admin.site.urls),
]

# Without GraphQL App URLS
urlpatterns += [
    path('', include('wgql.urls'))
]
