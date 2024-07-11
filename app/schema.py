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
    products = graphene_django.DjangoListField(ProductType)
    images = graphene_django.DjangoListField(ImageType)
    orders = graphene_django.DjangoListField(OrderType)

    product = graphene.Field(
        ProductType, id=graphene.Int(required=True))

    def resolve_product(root, info, id):
        return models.Product.objects.get(pk=id)

    order = graphene.Field(
        OrderType, id=graphene.Int(required=True))

    def resolve_order(root, info, id):
        return models.Order.objects.get(pk=id)


schema = graphene.Schema(query=Query)
