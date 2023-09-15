from functools import wraps
from flask import request,make_response,jsonify,g
import jwt
class JWTMiddleware:
    def confirm_token(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            token = request.headers.get("Authorization")
            print(token)
            print('---')
            if not token:
                return err_response("token required",401)
            
            try:
                payload = jwt.decode(token,'yu023468',algorithms='HS256')
                print(payload)
                return func(*args, **kwargs)
            except jwt.ExpiredSignatureError:
                return err_response("Token expired",401)
            except jwt.InvalidTokenError:
                return err_response("Invalid token",401)
            
            
    
        return wrap

def err_response(err: str,code: int):
    return make_response(
            jsonify(
                {
                    "success":False,
                    "message":err
                }
            ),
            code)
