import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField

from .cards.schema.queries import CardConnectionField, CardConnection
from .cards.schema.mutations import CreateCardMutation, UpdateCardMutation


class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_cards = SQLAlchemyConnectionField(CardConnection)
    filter_cards = CardConnectionField(CardConnection, args={
        'title': graphene.Argument(graphene.String),
        'action': graphene.Argument(graphene.String),
    })


class Mutation(graphene.ObjectType):
    create_card = CreateCardMutation.Field()
    update_card = UpdateCardMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
