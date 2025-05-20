from flask import redirect

from app import load_app_languages
from . import general

app_language_code = 'hr'

@general.route('/language/<choosen_language_code>')
def language(choosen_language_code):
    global app_language_code
    app_language_code = choosen_language_code
    print(id(app_language_code))
    return redirect('/')

@general.route('/language/reload')
def reload_language():
    global app_languages
    app_languages = load_app_languages(__file__)
    return '<html>RELOADED TRANSLATION</html>'