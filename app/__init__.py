from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from flask_cors import CORS

# configure db
db = SQLAlchemy()
migrate = Migrate()
load_dotenv()


def create_app(test_config=None):
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    if not test_config:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")
    else:
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_TEST_DATABASE_URI")

    # import models here
    from app.models.investor import Investor
    from app.models.transaction import Transaction
    from app.models.stock import Stock
    from app.models.exchange import Exchange


    db.init_app(app)
    migrate.init_app(app, db)

    # register Blueprints here
    from .investor_routes import investor_bp
    app.register_blueprint(investor_bp)

    from .investor_routes import transaction_bp
    app.register_blueprint(transaction_bp)

    from .investor_routes import stock_bp
    app.register_blueprint(stock_bp)

    from .exchange_routes import exchange_bp
    app.register_blueprint(exchange_bp)


    CORS(app)
    return app