from flask import render_template

from app import load_app_languages
from . import program

app_languages = load_app_languages(__file__)

@program.route('/')
def program():
    from app.general.language import app_language_code
    return render_template('program.html', **app_languages.get(app_language_code, {}))
