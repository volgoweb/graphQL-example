import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from ..models import Card


class CardNode(SQLAlchemyObjectType):
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
        return qs
