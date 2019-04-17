import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.functions import now
from ..database import db


# Base = declarative_base()
Base = db.Model
# sa = db

CARD_MODEL_TBL_NAME = 'cards_cards'
ACTION_MODEL_TBL_NAME = 'cards_actions'


card_actions = sa.Table(
    'cards_m2m_card_action',
    Base.metadata,
    sa.Column('card_id', sa.Integer, sa.ForeignKey('%s.id' % CARD_MODEL_TBL_NAME)),
    sa.Column('action_id', sa.Integer, sa.ForeignKey('%s.id' % ACTION_MODEL_TBL_NAME)),
)


class Card(Base):
    __tablename__ = CARD_MODEL_TBL_NAME

    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String(250), nullable=False)
    created_at = sa.Column(sa.DateTime(timezone=True), server_default=now())
    # actions_count = sa.Column(sa.Integer, nullable=False, default=0, index=True)
    actions = sa.orm.relationship('Action', secondary=card_actions)

    def __repr__(self):
        return self.title


class Action(Base):
    __tablename__ = ACTION_MODEL_TBL_NAME

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(200), unique=True, nullable=False)

    def __repr__(self):
        return self.name
