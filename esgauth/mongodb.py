from pymongo import MongoClient
from flask import has_app_context, current_app as app
class MongoDB:
    _instance = None
    _client = None
    _db = None

    def __new__(cls, ):
        print('==== MongoDB NEW Called')
        if cls._instance is None:
            print("===  MongoDB NEW IS NONE")
            cls._instance = super(MongoDB, cls).__new__(cls)
        return cls._instance
    
    @classmethod
    def _initialize(cls):
        print('======== MongoDB INIT IS CALLED')
        if not has_app_context():
            raise RuntimeError("Application context required for MongoDB initialization")
        
        if cls._instance._client is None or cls._instance._db is None:
            print('=== MongoDB VARS ARE NONE')
            cls._instance._client = MongoClient(app.config['MONGO_URI'])
            cls._instance._db = cls._instance._client.get_default_database()

    @classmethod
    def create_instance(cls):
        instance = cls.__new__(cls)
        instance._initialize()

    @classmethod
    def get_user(cls, query):
        cls.create_instance()

        return cls._instance._db.users.find_one(query)
