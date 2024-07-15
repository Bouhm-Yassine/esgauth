from flask import current_app as app

from .mongodb import MongoDB
from .azure_ad_auth import AzureADAuth


with app.app_context():
    AzureADAuth(app.config['AZURE_CLIENT_ID'], app.config['AZURE_AUTHORITY'])
    MongoDB(app.config['MONGO_URI'])