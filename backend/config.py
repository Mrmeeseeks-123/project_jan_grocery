import os

class BaseConfig:
    SQL_ALCHEMY_TRACK_MODIFICATIONS=False

class LocalDevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI="sqlite:///database.sqlite3"
    DEBUG=True
    SECRET_KEY=os.environment.get("SECRET_KEY")
    SECURITY_PASSWORD_SALT=os.environment.get("SECURITY_PASSWORD_SALT")

class ProductionConfig(BaseConfig):
    DEBUF=False