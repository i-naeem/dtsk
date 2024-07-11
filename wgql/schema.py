import graphene
import graphene_django
from wgql import models


class ProductType(graphene_django.DjangoObjectType):
    class Meta:
        model = models.Product
        fields = ["id", "product_name", "product_quantity", "product_price"]


class Query(graphene.ObjectType):
    product = graphene.Field(ProductType, id=graphene.BigInt())
    products = graphene_django.DjangoListField(ProductType)

    def resolve_product(root, info, id):
        return models.Product.objects.get(pk=id)


schema = graphene.Schema(query=Query)
