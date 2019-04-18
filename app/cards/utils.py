from .models import Action


def find_actions_by_name(names):
    actions = Action.query.filter(Action.name.in_(names)).all()
    return actions
