# mongodb.py
import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Load environment variables from .env file
load_dotenv()

class MongoDB:
    def __init__(self):
        # Get MongoDB URI from environment variables
        mongo_uri = os.getenv('MONGO_URI')
        if not mongo_uri:
            raise ValueError('MongoDB URI not found in environment variables')

        self.client = MongoClient(mongo_uri)
        self.db = self.client.get_default_database()

    def get_user(self, user_id):
        return self.db.users.find_one({'_id': user_id})
