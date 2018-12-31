from flask import Flask
from app.config import Base
from app.changes import changes
from app.entries import entries
from app.languages import languages
from app.searches import searches
from app.tags import tags
from app.users import users


from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Base)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(changes)
    app.register_blueprint(entries)
    app.register_blueprint(languages)
    app.register_blueprint(searches)
    app.register_blueprint(tags)
    app.register_blueprint(users)

    return app

