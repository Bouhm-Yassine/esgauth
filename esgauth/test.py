import os

def read_env():
    print('====== READ')
    print(os.getenv('MONGO_URI'))