from flask import Flask
from flask_graphql import GraphQLView

from .database import db
from .cards.models import Card, Action
from .schema import schema


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../db.sqlite3'
    db.init_app(app)

    @app.route('/')
    def hello_world():
        rows = db.session.query(Card)
        cards = ['<p>%s</p>' % c.title for c in rows]
        return ''.join(cards)

    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True  # for having the GraphiQL interface
        )
    )

    return app
