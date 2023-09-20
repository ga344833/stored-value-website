from .UserService import UserService 
from  .dtos import loginDto,registerDto,perfectInfoDto,ImageDto
from flask import request,make_response,jsonify,g
class UserController:
    def __init__(self):
        self.UserService = UserService()

    def login(self):
        print('--UserController stage--')
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
            
            token = self.UserService.generate_token(result[0])
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
                        "success":False,
                        "message":"no user info"
                    }
                ),
                400
            )

    def create(self):
        print('--UserController stage--')
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
        print('--UserController stage--')
        result = self.UserService.getCustomersInfo()
        return result
        
    def getCustomerInfo(self,customer_id):
        print('--UserController stage--')
        servicer_id = g.token.get('sub')
        print("servicer_id : "+str(servicer_id))
        if servicer_id == 1: ## 篩選是否為客服人員、避免API被盜用、後續再規劃
            result = self.UserService.getCustomerById(customer_id)
            return result 
        else:
            return make_response(jsonify({'success':False,'message':'Non service staff'}))

    def get_customer_profile(self):      
        print('--UserController stage--')
        try:
            # 从 JWT token 中获取客户的用户 ID
            customer_id = g.token.get('sub')
            print("customer_id : "+str(customer_id))
            # 使用 customer_id 查询客户的个人信息
            customer_info = self.UserService.getCustomerById(customer_id)
            # print(customer_info)
            if customer_info:
                return make_response(
                jsonify(
                    {   "success": True,
                        "customer": customer_info
                    }
                ),
            )
            else:
                return make_response(jsonify({'success':False,'message':"Customer not found"}),404)
        except Exception as e:
            return make_response(jsonify({'success':False,'message':str(e)}))

    def patch_customer_profile(self):      
        try:
            # 从 JWT token 中获取客户的用户 ID
            customer_id = g.token.get('sub')
            print("customer_id : "+str(customer_id))
            # 使用 customer_id 查询客户的个人信息
            if request.is_json:
                data = request.get_json()
                country = data.get("country")
                idtype = data.get("idtype")
                idnumber = data.get("idnumber")
                dto = perfectInfoDto(customer_id,country , idtype , idnumber)
                print(dto.customer_id)
            patch_customer_info = self.UserService.patchCustomerInfo(dto)
            if patch_customer_info:
                return make_response(
                jsonify(
                    {   "success": patch_customer_info['success'],
                        "message": patch_customer_info['message']
                    }
                ),
            )
            else:
                return make_response(jsonify({'success':False,'message':"Customer not found"}),404)
        except Exception as e:
            return make_response(jsonify({'success':False,'message':str(e)}),500)

    def upload_image(self):
        print('--UserController stage--')
        try:
            # 从 JWT token 中获取客户的用户 ID
            customer_id = g.token.get('sub')
            print("customer_id : "+str(customer_id))
            # 使用 customer_id 查询客户的个人信息
            if 'file' not in request.files:
                return make_response(jsonify({'success': False, 'message': 'No file part'}), 400)
            file = request.files['file']
            # 检查文件名是否为空
            if file.filename == '':
                return make_response(jsonify({'success': False, 'message': 'No selected file'}), 400)
            dto = ImageDto(customer_id,file)
            upload_info = self.UserService.uploadInfo(dto)
            #patch_customer_info = self.UserService.patchCustomerInfo(dto)
            if upload_info:
                return make_response(
                jsonify(
                    {   "success": upload_info['success'],
                        "message": upload_info['message']
                    }
                ),
            )
            else:
                return make_response(jsonify({'success':False,'message':"Customer not found"}),404)
        except Exception as e:
            return make_response(jsonify({'success':False,'message':str(e)}),500)