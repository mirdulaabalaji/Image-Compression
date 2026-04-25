from flask import Flask
from flask_cors import CORS
from .routes import bp

def create_app():
    app = Flask(__name__)

    app.config['DEBUG'] = True

    # ✅ Allow React frontend
    CORS(app, resources={
        r"/*": {
            "origins": ["http://localhost:5173"]
        }
    })

    app.register_blueprint(bp)

    return app