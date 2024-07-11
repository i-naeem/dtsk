from graphene_file_upload.django import FileUploadGraphQLView
from django.views.decorators.csrf import csrf_exempt
from django.urls import path
from . import views
from .schema import schema

app_name = "app"
urlpatterns = [
    path("", views.index, name="index"),
    path("graphql", csrf_exempt(
        FileUploadGraphQLView.as_view(graphiql=True, schema=schema))),

    path("order/<int:order_id>", views.order, name="order"),
    path("create_order", views.create_order, name="create_order"),

    path("product/<int:product_id>", views.product, name="product"),
    path("create_product", views.create_product, name="create_product"),
]
