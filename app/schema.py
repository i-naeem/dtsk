import graphene_django
from . import models
import graphene


class ImageType(graphene_django.DjangoObjectType):
    class Meta:
        model = models.Image
        fields = ("id", "image")


class ProductType(graphene_django.DjangoObjectType):
    images = graphene_django.DjangoListField(ImageType)

    class Meta:
        model = models.Product
        fields = ("id", "name", "price", "quantity", "images")

    def resolve_images(root, info):
        return root.images.all()


class OrderType(graphene_django.DjangoObjectType):
    products = graphene_django.DjangoListField(ProductType)

    class Meta:
        model = models.Order
        fields = ("id", "created_at", "products")

    def resolve_products(root, info):
        return root.order.all()


class Query(graphene.ObjectType):
    all_products = graphene_django.DjangoListField(ProductType)
    all_images = graphene_django.DjangoListField(ImageType)
    all_orders = graphene_django.DjangoListField(OrderType)


schema = graphene.Schema(query=Query)
