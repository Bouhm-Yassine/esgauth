from pymongo import MongoClient

class MongoDB:
    def __init__(self, mongo_uri=None):
        # Get MongoDB URI from environment variables
        if not mongo_uri:
            raise ValueError('MongoDB URI not found in environment variables')

        self.client = MongoClient(mongo_uri)
        self.db = self.client.get_default_database()

    def get_user(self, user_id):
        return self.db.users.find_one({'_id': user_id})
