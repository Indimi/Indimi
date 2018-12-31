import os

class Base:
    PROJECT_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    TESTING = False
    SECRET_KEY = "Hello"

    DATABASE_USER = 'indimi'
    DATABASE_PASSWORD = 'indimi'
    DATABASE_DB = 'indimi'
    DATABASE_TABLE_PREFIX = 'rw_'

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{DATABASE_USER}:{DATABASE_PASSWORD}@localhost:3306/{DATABASE_DB}"
