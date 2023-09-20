from .UserRepo import UserRepo
from .dtos import registerDto,loginDto,perfectInfoDto,ImageDto
import jwt
from datetime import datetime, timedelta
import base64
class UserService:
    def __init__(self):
        self.UserRepo = UserRepo()

    def create(self , dto:registerDto):
        dto.check()
        result = self.UserRepo.create(dto.fullname , dto.phone , dto.email , dto.username , dto.password , dto.gender)
        return result

    # 先依照username找出user 再比對密碼
    def login(self , dto:loginDto):
        dto.check()
        userinfo = self.UserRepo.getUserByName(dto.userName)
        if userinfo.password != dto.passWord:
            return [userinfo,2]
        if userinfo.internal == '0': 
            return [userinfo,0]
        if userinfo.internal == '1':
            print(userinfo.fullname +" is servicer")
            return [userinfo,1]
    
    def getCustomersInfo(self):
        CustomersInfo = self.UserRepo.getCustomersInfo()
        return CustomersInfo

    def patchCustomerInfo(self,dto:perfectInfoDto):
        dto.check()
        result = self.UserRepo.patchCustomerInfo(dto.customer_id , dto.country , dto.idtype , dto.idnumber)
        return result
    
    def uploadInfo(self,dto:ImageDto):
        dto.check()
        result = self.UserRepo.uploadInfo(dto.customer_id , dto.file)
        return result

    def getCustomerById(self, customer_id):
        customer = self.UserRepo.getCustomerById(customer_id)
        
        customer_info = {
            'id' : customer.id,
            'fullname': '',
            'phone': '',
            'email': '',
            'country': '',
            'idtype': '',
            'idnumber': '',
            'forzen':'',
            'gender':'',
            'profile_image':'',
            'state':''
            }
        if customer:
            customer_info['fullname'] = customer.fullname
            customer_info['phone'] = customer.phone
            customer_info['email'] = customer.email
            if 'country' in customer.__dict__:
                customer_info['country'] = customer.country
            if 'idtype' in customer.__dict__:
                customer_info['idtype'] = customer.idtype
            if 'idnumber' in customer.__dict__:
                customer_info['idnumber'] = customer.idnumber
            if 'profile_image' in customer.__dict__:
                try:
                    i2 = customer.profile_image
                    print("origin img:"+str(i2))
                    img = base64.b64encode(customer.profile_image).decode("utf-8")
                    print('img : '+str(img))
                    customer_info['profile_image'] = img
                except:
                    pass
            if 'forzen' in customer.__dict__:
                customer_info['forzen'] = customer.forzen
            if 'gender' in customer.__dict__:
                customer_info['gender'] = customer.gender
            if 'state' in customer.__dict__:
                customer_info['state'] = customer.state
        
        return customer_info
    
    # 生成 JWT 令牌
    def generate_token(self,user):
        payload = {
            'sub' : user.id,
            'exp' : datetime.utcnow() + timedelta(days=1),
            'iat' : datetime.utcnow()
        }
        token = jwt.encode(payload,'yu023468',algorithm='HS256')
        return token
    
    def perfectInfo(self,dto:perfectInfoDto):
        dto.check()
        result = self.UserRepo.perfectInfo(dto.country , dto.ID_type , dto.ID_number , dto.profile_image)
        return result
