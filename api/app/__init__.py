from flask import Flask
from flask_cors import CORS
from .routes import main as AppRoutes

def App():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(AppRoutes)
    return app