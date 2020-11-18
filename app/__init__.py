from flask import Flask
from flask_mongoengine import MongoEngineSessionInterface
from flask_debugtoolbar import DebugToolbarExtension

from app.views import rst
from app.models import db


def create_app(configs):
    app = Flask(__name__)
    app.register_blueprint(rst)
    app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
    app.config['MONGO_DBNAME'] = 'SomeCollection'
    app.config['SECRET_KEY'] = 'secret_key'
    db.init_app(app)
    app.session_interface = MongoEngineSessionInterface(db)
    toolbar = DebugToolbarExtension(app)
    return app
