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


if __name__ == "__main__":
    manager.run()
