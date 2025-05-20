from flask import render_template

from app import load_app_languages
from . import general

app_languages = load_app_languages(__file__)

@general.route('/privacy_policy')
def privacy_policy():
    from app.general.language import app_language_code
    return render_template('privacy_policy.html', **app_languages.get(app_language_code, {}))

@general.route('/about')
def about():
    from app.general.language import app_language_code
    print('----\n', app_language_code)
    print(app_languages.get(app_language_code, {}))
    return render_template('about.html', **app_languages.get(app_language_code, {}))

@general.route('/')
def main():
    from app.general.language import app_language_code
    return render_template('home.html', **app_languages.get(app_language_code, {}))
 