from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Just like in Derek's fakebook, this is where the ORM is established.
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Note to self: When you make a new blueprint, make sure to register it here.
    from app.blueprints.authentication import bp as authentication
    from app.blueprints.main import bp as main
    app.register_blueprint(authentication)
    app.register_blueprint(main)