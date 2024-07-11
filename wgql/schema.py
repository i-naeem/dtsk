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


class ProductMutation(graphene.Mutation):
    class Arguments:
        product_name = graphene.String(required=True)
        product_quantity = graphene.Int(required=True)
        product_price = graphene.Float(required=True)

    product = graphene.Field(ProductType)

    @classmethod
    def mutate(cls, root, info, product_name, product_quantity, product_price):
        product = models.Product(
            product_name=product_name,
            product_quantity=product_quantity,
            product_price=product_price
        )

        product.save()

        return ProductMutation(product=product)


class Mutation(graphene.ObjectType):
    create_product = ProductMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
