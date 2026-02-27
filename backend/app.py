from flask import Flask
from models import db
from config import LocalDevelopmentConfig
from dotenv import load_dotenv

def create_app():

    app=Flask(__name__)
    load_dotenv()
    app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app

app=create_app()

if __name__=="__main__":
    app.run()
