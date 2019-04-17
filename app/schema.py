import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField

from .cards.schema.queries import CardConnectionField, CardConnection


class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_cards = SQLAlchemyConnectionField(CardConnection)
    filter_cards = CardConnectionField(CardConnection, args={
        'title': graphene.Argument(graphene.String),
    })


schema = graphene.Schema(query=Query)
