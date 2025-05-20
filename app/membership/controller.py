from flask import render_template

from app import load_app_languages 
from . import membership

app_languages = load_app_languages(__file__)

@membership.route('/')
def membership():
    from app.general.language import app_language_code
    print('---\n', app_language_code)
    print(app_languages)
    return render_template('membership.html', **app_languages.get(app_language_code, {}))