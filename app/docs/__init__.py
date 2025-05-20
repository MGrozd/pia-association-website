from flask import Blueprint

documents = Blueprint(
    name='documents', 
    import_name=__name__,
)

from . import controller