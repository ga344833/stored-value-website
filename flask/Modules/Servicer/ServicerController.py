from .ServicerService import ServicerService 
# from  .dtos import loginDto,registerDto
from flask import request,make_response,jsonify
import json
class ServicerController:
    def __init__(self):
        self.ServicerService = ServicerService()
    

    ## 待辦 : 可以做一個 緩存 存取登入的service 是誰 ，然後當他進行任何操作時，都要先核對一次他是不是 service ，確保資料不會被駭入
    def getUserinfo(self): 
        try:
            print("--1--")
            user_info_list = self.ServicerService.getuserinfo()
            user_info_json = json.dumps(user_info_list)
            response = make_response(jsonify({"success":True,"user_info":user_info_json}))
            response.headers["Content-Type"] = "application/json"
            return response
        except Exception as msg:
            print(msg)
            return make_response(
                jsonify(
                    {
                        "success":"false",
                        "message":str(msg)
                    }
                ),
                400
            )

    # def login(self):
    #     try:
    #         if request.is_json:
    #             params = request.get_json()
    #             userName = params.get('username', None)
    #             passWord = params.get('password', None)
    #             print('username : '+str(userName))
    #             print('passWord : '+str(passWord))
    #             dto = loginDto(userName , passWord)
    #         else:
    #             raise ValueError('data type error')    

    #         result = self.UserService.login(dto)
    #         return make_response(
    #             jsonify(
    #                 {
    #                     "success":"true",
    #                     "message":str(result),
    #                     "code": result
    #                 }
    #             )
    #         )
    #     except Exception as msg:
    #         print(msg)
    #         return make_response(
    #             jsonify(
    #                 {
    #                     "success":"false",
    #                     "message":str(msg)
    #                 }
    #             ),
    #             400
    #         )

    # def create(self):
    #     try:
    #         if request.is_json:
    #             data = request.get_json()
    #             fullname = data.get("fullname")
    #             phone = data.get("phone")
    #             email = data.get("email")
    #             username = data.get("username")
    #             password = data.get("password")
    #             gender = data.get("gender")
    #             dto = registerDto(fullname , phone , email , username , password , gender)
    #         else:
    #             raise ValueError('data type error')    

    #         result = self.UserService.create(dto)
            
    #         return make_response(
    #             jsonify(
    #                 {
    #                     "success":result,
    #                     "message":str(fullname)+" success create"
    #                 }
    #             ),
    #         )
    #     except Exception as msg:
    #         return make_response(
    #             jsonify(
    #                 {
    #                     "success":"false",
    #                     "message":str(msg)
    #                 }
    #             ),
    #             400
    #         )
