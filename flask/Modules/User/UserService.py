from .UserRepo import UserRepo
from .dtos import registerDto,loginDto,perfectInfoDto
import jwt
from datetime import datetime, timedelta
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
    
    def getCustomerById(self, customer_id):
        customer = self.UserRepo.getCustomerById(customer_id)
        return customer
    
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
