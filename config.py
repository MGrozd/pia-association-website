class Config(object):
    pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    SECRET_KEY = 'secretkey'
    RECAPTCHA_PUBLIC_KEY = None
    RECAPTCHA_PRIVATE_KEY = None
    MAIL_SUBJECT_PREFIX = '[Svijet mirisa]'
    MAIL_SENDER = 'Svijet mirisa Admin <flasky@example.com>'

    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.sqlite'
    # SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg2://user:password@ip:port/db_name'