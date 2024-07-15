from pymongo import MongoClient
from flask import has_app_context, current_app as app
class MongoDB:
    _instance = None

    def __new__(cls, ):
        if cls._instance is None:
            cls._instance = super(MongoDB, cls).__new__(cls)
        return cls._instance
    
    @classmethod
    def _initialize(cls):
        if not has_app_context():
            raise RuntimeError("Application context required for MongoDB initialization")
        
        if cls._client is None or cls._db is None:
            cls._client = MongoClient(app.config['MONGO_URI'])
            cls._db = cls._client.get_default_database()

    @classmethod
    def get_db(cls):
        if cls._db is None:
            cls._initialize()
        return cls._db
    
    @classmethod
    def get_user(cls, query):
        db = cls.get_db()
        return db.users.find_one(query)
