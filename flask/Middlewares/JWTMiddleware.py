from functools import wraps
from flask import request,make_response,jsonify,g
import jwt
class JWTMiddleware:
    def confirm_token(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            auth_header = request.headers.get("Authorization")
            print(auth_header)
            print('---')
            if not auth_header:
                return err_response("token required",401)
            if auth_header and auth_header.startswith('Bearer '):
                # 提取 token，移除 'Bearer ' 前缀
                token = auth_header.split('Bearer ')[1]
            try:
                payload = jwt.decode(token,'yu023468',algorithms=['HS256'])
                g.token = payload
                print(payload)
                # print(func(*args, **kwargs))
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
