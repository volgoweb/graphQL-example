import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField

from .cards.schema.queries import CardConnectionField, CardConnection
from .cards.schema.mutations import CardMutation, CardMutation


class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_cards = SQLAlchemyConnectionField(CardConnection)
    filter_cards = CardConnectionField(CardConnection, args={
        'title': graphene.Argument(graphene.String),
    })


class Mutation(graphene.ObjectType):
    create_card = CardMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
