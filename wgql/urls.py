from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("create/product", views.create_product, name="create_product"),
    path("create/images", views.create_images, name="create_images"),
    path("create/order", views.create_order, name="create_order"),
]
