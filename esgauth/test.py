from flask import current_app as app

def test():
    print('====== READ ENV')
    print(app.config['MONGO_URI'])