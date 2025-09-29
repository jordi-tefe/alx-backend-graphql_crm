import graphene
from crm.schema import Query as CRMQuery, Mutation as CRMMutation

class Query(CRMQuery, graphene.ObjectType):
    pass

class Mutation(CRMMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
import graphene
from crm.models import Product

class UpdateLowStockProducts(graphene.Mutation):
    class Arguments:
        pass

    success = graphene.Boolean()
    updated_products = graphene.List(graphene.String)

    def mutate(root, info):
        low_stock = Product.objects.filter(stock__lt=10)
        updated_names = []
        for p in low_stock:
            p.stock += 10
            p.save()
            updated_names.append(f"{p.name} ({p.stock})")
        return UpdateLowStockProducts(success=True, updated_products=updated_names)

class Mutation(graphene.ObjectType):
    update_low_stock_products = UpdateLowStockProducts.Field()
