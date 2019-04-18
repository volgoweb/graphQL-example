import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from graphene.relay import ClientIDMutation

from ..models import Card, Action
from ..utils import find_actions_by_name
from .queries import CardNode
from ...database import db


class CreateCardInput(graphene.InputObjectType, CardNode):
    class Meta:
        model = Card


class CardMutation(graphene.Mutation):
    card = graphene.Field(lambda: CardNode, description="Card created by this mutation.")

    class Arguments:
        title = graphene.String(required=True)
        action_names = graphene.List(graphene.String)

    @classmethod
    def mutate(cls, root, info, **input):
        card = Card(title=input['title'])
        if 'action_names' in input:
            actions = find_actions_by_name(input['action_names'])
            actions_by_name = {a.name: a for a in actions}
            for name in input['action_names']:
                if name in actions_by_name:
                    action = actions_by_name[name]
                else:
                    action = Action(name=name)
                    db.session.add(action)
                card.actions.append(action)
        db.session.add(card)
        db.session.commit()
        return CardMutation(card=card)
