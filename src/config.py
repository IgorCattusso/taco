# Standard Library
import os

# Third-Party Libraries
from dotenv import load_dotenv

class Config:
    def __init__(self):
        load_dotenv()
        self.database_host = os.environ.get('DATABASE_HOST', '')
        self.database_port = os.environ.get('DATABASE_PORT', '')
        self.database_name = os.environ.get('DATABASE_NAME', '')
        self.database_user = os.environ.get('DATABASE_USER', '')
        self.database_password = os.environ.get('DATABASE_PASSWORD', '')
