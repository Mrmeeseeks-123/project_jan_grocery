from flask import Flask
from models import db,User,Role
from config import LocalDevelopmentConfig
from dotenv import load_dotenv
from extensions import security
from flask_security import SQLAlchemyUserDatastore

def create_app():

    app=Flask(__name__)
    load_dotenv()
    app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    datastore=SQLAlchemyUserDatastore(db,User,Role)
    security.init_app(app,datastore=datastore)
    app.datastore=datastore


    with app.app_context():
        db.create_all()
    return app

app=create_app()

if __name__=="__main__":
    app.run()
