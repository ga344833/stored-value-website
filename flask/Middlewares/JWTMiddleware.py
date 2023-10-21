from functools import wraps
from flask import request,make_response,jsonify,g
import jwt
class JWTMiddleware:
    def confirm_token(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            auth_header = request.headers.get("Authorization")
            if not auth_header:
                return err_response("token required", 401)
            if auth_header and auth_header.startswith('Bearer '):
                token = auth_header.split('Bearer ')[1]
            try:
                payload = jwt.decode(token, 'yu023468', algorithms=['HS256'])
                g.token = payload
                return func(*args, **kwargs)
            except jwt.ExpiredSignatureError:
                return err_response("Token expired", 401)
            except jwt.InvalidTokenError:
                return err_response("Invalid token", 401)
        return wrap
    
    def check_internal(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            internal_type = g.token.get('internal_type')
            print(internal_type)
            if internal_type != 1:
                return err_response("Unauthorized", 403)
            return func(*args, **kwargs)
        return wrap
    
    def get_JWT_userid(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            user_id = g.token.get('user_id')
            return func(user_id,*args, **kwargs)
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
