import graphene
import graphene_django
from wgql import models


class ProductImagesType(graphene_django.DjangoObjectType):
    class Meta:
        model = models.ProductImages


class ProductType(graphene_django.DjangoObjectType):
    class Meta:
        model = models.Product
        images = graphene_django.DjangoListField(ProductImagesType)

        def resolve_images(root, info):
            return models.Product.objects.prefetch_related('images').all()


class Query(graphene.ObjectType):
    product = graphene.Field(ProductType, id=graphene.BigInt())
    products = graphene_django.DjangoListField(ProductType)

    def resolve_product(root, info, id):
        return models.Product.objects.prefetch_related("images").get(pk=id)


schema = graphene.Schema(query=Query)
