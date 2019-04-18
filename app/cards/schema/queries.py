import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from ..models import Card, Action


class ActionNode(SQLAlchemyObjectType):
    class Meta:
        model = Action
        interfaces = (graphene.relay.Node,)


class CardNode(SQLAlchemyObjectType):
    actions = SQLAlchemyConnectionField(ActionNode)

    class Meta:
        model = Card
        interfaces = (graphene.relay.Node,)


class CardConnection(graphene.Connection):
    class Meta:
        node = CardNode


class CardConnectionField(SQLAlchemyConnectionField):
    @classmethod
    def get_query(cls, model, info, **kwargs):
        qs = SQLAlchemyConnectionField.get_query(model, info, **kwargs)
        if 'title' in kwargs:
            qs = qs.filter(Card.title.contains(kwargs['title']))
        if 'action' in kwargs:
            qs = qs.filter(Card.actions.any(name=kwargs['action']))
        return qs
