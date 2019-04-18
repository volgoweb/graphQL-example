import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from graphene.relay import ClientIDMutation

from ..models import Card
from .queries import CardNode
from ...database import db


class CreateCardInput(graphene.InputObjectType, CardNode):
    class Meta:
        model = Card


class CardMutation(graphene.Mutation):
    card = graphene.Field(lambda: CardNode, description="Card created by this mutation.")

    class Arguments:
        title = graphene.String(required=True)

    @classmethod
    def mutate(cls, root, info, **input):
        card = Card(title=input['title'])
        db.session.add(card)
        db.session.commit()
        return CardMutation(card=card)
