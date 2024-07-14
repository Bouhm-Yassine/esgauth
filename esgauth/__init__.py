from .mongodb import MongoDB
from .azure_ad_auth import AzureADAuth


MONGO_URI = "mongodb://localhost:27017/esg-db-bkam?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&ssl=false"
AZURE_CLIENT_ID = "87c712c6-82bd-4510-9b9f-12d4ca8a9259"
AZURE_AUTHORITY = "https://login.microsoftonline.com/d6f9c526-4b38-42bb-b2fd-491f492591db"
    

AzureADAuth(AZURE_CLIENT_ID, AZURE_AUTHORITY)
MongoDB(MONGO_URI)