from django.urls import path
from . import views

app_name = "app"
urlpatterns = [
    path("", views.index, name="index"),
    path("order/<int:order_id>", views.order, name="order"),
    path("create_order", views.create_order, name="create_order"),

    path("product/<int:product_id>", views.product, name="product"),
    path("create_product", views.create_product, name="create_product"),
]
