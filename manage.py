from flask_script import Shell, Manager
from flask import current_app

from app.database import db
from app.cards import models
from app import create_app

manager = Manager(create_app)


@manager.command
def create_db():
    db.init_app(current_app)
    db.create_all()

    # card = models.Card(title='dfd2f')
    # add_action = models.Action(name='add')
    # remove_action = models.Action(name='remove')
    # card.actions.append(add_action)
    # card.actions.append(remove_action)
    # db.session.commit()


if __name__ == "__main__":
    manager.run()
