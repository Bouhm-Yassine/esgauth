from pymongo import MongoClient
from flask import current_app as app
class MongoDB:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MongoDB, cls).__new__(cls)

            cls._instance.client = MongoClient(app.config['MONGO_URI'])
            cls._instance.db = cls._instance.client.get_default_database()

        return cls._instance
    

    @classmethod
    def get_user(cls, query):
        return cls._instance.db.users.find_one(query)
