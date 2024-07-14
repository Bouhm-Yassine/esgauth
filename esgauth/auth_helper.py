from flask import g
from .mongodb import MongoDB


class AuthHelper:
    @staticmethod
    def get_logged_in_user():
        user_email = g.decoded_token['preferred_username'].lower()
        if not isinstance(user_email, str):
            return {"status": "fail", "message": "No email found"}, 400
        
        user = MongoDB.get_user({'email': user_email})
        if not user:
            return {"status": "fail", "message": "No such user with the provided email"}, 404

        return user, 200
