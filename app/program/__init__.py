from flask import Blueprint

program = Blueprint(
    name='program', 
    import_name=__name__,
    template_folder='templates/program',
)

from . import controller