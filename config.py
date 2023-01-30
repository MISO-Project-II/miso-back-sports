import os
from dotenv import load_dotenv

dotenv_file_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_file_path):
    load_dotenv(dotenv_file_path)
    
class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    ENV = "development"
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:admin@localhost:5433/db_sportapp"

class ProductionConfig(Config):
    ENV = "production"
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:miso-db-2023@34.173.63.65:5432/db_sportapp"
