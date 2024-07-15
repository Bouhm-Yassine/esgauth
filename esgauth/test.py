from flask import current_app as app
import os

def read_env():
    print('====== READ')
    print(os.getenv('MONGO_URI'))
    print(app.config['MONGO_URI'])