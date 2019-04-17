from flask import Flask

from .database import db
from .cards.models import Card, Action


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../db.db'
    db.init_app(app)


    @app.route('/')
    def hello_world():
        rows = db.session.query(Card)
        cards = ['<p>%s</p>' % c.title for c in rows]
        return ''.join(cards)


    @app.route('/add')
    def add():
        card = Card(title='dfd2f')
        db.session.add(card)
        db.session.commit()
        return str(card.id)

    return app
