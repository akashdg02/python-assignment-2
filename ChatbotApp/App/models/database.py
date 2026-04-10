from flask_sqlalchemy import SQLAlchemy

# Initialize the SQLAlchemy object
# This MUST be named 'db' to match your import statement in __init__.py
db = SQLAlchemy()

# This is a helper function to initialize the database with your Flask app
def init_db(app):
    db.init_app(app)
    with app.app_context():
        # This creates the .db file and the tables based on your models
        db.create_all()