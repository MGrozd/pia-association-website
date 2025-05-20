from flask import Blueprint

general = Blueprint(
    name='general', 
    import_name=__name__,
    template_folder='templates/general',
)

from . import controller
from . import language