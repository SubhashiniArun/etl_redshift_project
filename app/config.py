import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID', 'default-secret-key')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY', 'default-secret-key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', "mysql+pymysql://root:checkmysql@localhost:3306/etl_project")

def get_config(environment="development"):
    if environment == "development":
        return DevelopmentConfig