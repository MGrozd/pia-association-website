from pathlib import Path
import json

from flask import Flask
import yaml

from config import DevConfig

languages_code = ['hr', 'en', 'de']
languages_folder_name = 'languages'

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevConfig)

    from .general import general as general_blueprint
    app.register_blueprint(general_blueprint, url_prefix='/')

    from .membership import membership as membership_blueprint
    app.register_blueprint(membership_blueprint, url_prefix='/membership')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .docs import documents as docs_blueprint
    app.register_blueprint(docs_blueprint, url_prefix='/docs')

    from .program import program as program_blueprint
    app.register_blueprint(program_blueprint, url_prefix='/program')

    return app


def load_app_languages(path):
    app_languages = {}
    for language_code in languages_code:
        file_name = language_code + '.yaml'  #'.json'
        file_path = Path(path).parent / languages_folder_name / file_name
        if file_path.exists():
            with open(file_path, 'r', encoding='utf8') as file:
                app_languages[language_code] = yaml.safe_load(file) #json.load(file)
    return app_languages
