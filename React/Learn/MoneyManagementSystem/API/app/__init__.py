from flask import Flask
from .config import Config
from .models import db
from flask_cors import CORS

def create_app():
    app = Flask(__name__)

    CORS(app,resources={r"/*":{"origins":"*"}})

    app.config.from_object(Config)

    db.init_app(app)

    from app.routes import init_routes
    init_routes(app)

    return app