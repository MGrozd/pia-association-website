from flask import Blueprint

membership = Blueprint(
    name='membership', 
    import_name=__name__,
    template_folder='templates/membership',
)

from . import controller