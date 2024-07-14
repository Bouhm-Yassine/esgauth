from functools import wraps
from flask import request, g

from .azure_ad_auth import AzureADAuth
from .auth_helper import AuthHelper

def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            # Decode token and store it in the request object
            g.decoded_token = AzureADAuth.decode_token()
            
            # Check if X-Required-Roles header exists and authorize based on roles
            required_roles = request.headers.get("X-Required-Roles", None)
            if required_roles:
                required_roles = required_roles.split(",")
                
                # Ensure required_roles is not an empty list
                if required_roles:
                    # Retrieve logged-in user data
                    data, status = AuthHelper.get_logged_in_user()

                    if status != 200:
                        g.decoded_token = None
                        return data, status
                    
                    user_role = data['role']
                    if not user_role:
                        return {'status': 'fail','message': 'User role not found.'}, 403
                    
                    if user_role not in required_roles:
                        return {'status': 'fail','message': 'Access denied.'}, 403
                

        except Exception as e:
            return {"status": "fail", "message": str(e)}, 401
        
        return f(*args, **kwargs)
    return decorated_function