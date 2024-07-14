from functools import wraps

from .azure_ad_auth import AzureADAuth

def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            # Decode token and store it in the request object
            decoded_token = AzureADAuth.decode_token()

            print('========= decoded_token', decoded_token)
            

        except Exception as e:
            return {"status": "fail", "message": str(e)}, 401
        
        return f(*args, **kwargs)
    return decorated_function