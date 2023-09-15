from .UserService import UserService 
from  .dtos import loginDto,registerDto, perfectInfoDto
from flask import request,make_response,jsonify,g

class UserController:
    def __init__(self):
        self.UserService = UserService()

    def login(self):
        try:
            if request.is_json:
                params = request.get_json()
                userName = params.get('username', None)
                passWord = params.get('password', None)
                print('username : '+str(userName))
                print('passWord : '+str(passWord))
                dto = loginDto(userName , passWord)
            else:
                raise ValueError('data type error')    

            result = self.UserService.login(dto)
            if result[0]:
                token = self.UserService.generate_token(result[0])
            else:
                return make_response(jsonify({
                        "success":"false",
                        "message":"Authentication failed"
                    }),401)
            
            return make_response(
                jsonify(
                    {
                        "success":True,
                        "code":result[1],
                        "token":token,
                    }
                )
            )
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
            
            return make_response(
                jsonify(
                    {
                        "success":result,
                        "message":str(fullname)+" success create"
                    }
                ),
            )
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

    def getCustomersInfo(self):
        result = self.UserService.getCustomersInfo()
        return result  

    def get_customer_profile(self):      
        try:
            # 从 JWT token 中获取客户的用户 ID
            customer_id = g.token.get('sub')
            print(customer_id)
            # 使用 customer_id 查询客户的个人信息
            customer = self.UserService.getCustomerById(customer_id)
            if customer:
                return make_response(
                jsonify(
                    {
                        "success":True,
                        "customer":{"id":customer.id}
                    }
                ),
            )
            else:
                return make_response(jsonify({'success':False,'message':"Customer not found"}),404)
        except Exception as e:
            return make_response(jsonify({'success':False,'message':str(e)}))

    def PerfectInfo(self):
        try:
            if request.is_json:
                params = request.get_json()
                country = params.get('country', None)
                ID_type = params.get('ID_type', None)
                ID_number = params.get('ID_number', None)
                profile_image = params.get('profile_image', None)
                dto = perfectInfoDto(country , ID_type , ID_number , profile_image)
            else:
                raise ValueError('data type error')    

            result = self.UserService.perfectInfo(dto)
            return make_response(
                jsonify(
                    {
                        "success":True,
                        "code":result[0],
                        "customers_data": result[1],
                    }
                )
            )
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