from .UserService import UserService 
from  .dtos import loginDto,registerDto
from flask import request,make_response,jsonify

class UserController:
    def __init__(self):
        self.UserService = UserService()

    def login(self):
        try:
            if request.is_json:
                params = request.get_json()
                userName = params.get('userName', None)
                passWord = params.get('passWord', None)
                dto = loginDto(userName , passWord)
            else:
                raise ValueError('data type error')    

            result = self.UserService.login(dto)
        except Exception as msg:
            return make_response(
                jsonify(
                    {
                        "success":"false",
                        "message":str(msg)
                    }
                ),
                400
            )

    def create(self):
        try:
            if request.is_json:
                data = request.get_json()
                fullname = data.get("fullname")
                phone = data.get("phone")
                email = data.get("email")
                username = data.get("username")
                password = data.get("password")
                gender = data.get("gender")
                dto = registerDto(fullname , phone , email , username , password , gender)
            else:
                raise ValueError('data type error')    

            result = self.UserService.create(dto)
        except Exception as msg:
            return make_response(
                jsonify(
                    {
                        "success":"false",
                        "message":str(msg)
                    }
                ),
                400
            )