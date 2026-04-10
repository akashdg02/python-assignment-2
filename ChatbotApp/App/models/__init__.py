from flask import Flask
from .database import db

def create_app():
    app = Flask(__name__)
    
    # Database Configuration (using SQLite for simplicity)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the database with the app
    db.init_app(app)

    with app.app_context():
        # Import models here to ensure they are registered
        # from .models import User, Message 
        db.create_all()

    return app