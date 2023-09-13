from .UserRepo import UserRepo
from .dtos import registerDto,loginDto

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
            return [2,None]
        if userinfo.internal == '0': ## 等等把他修成 getuserinfo
            customers_data = self.UserRepo.getAllCustomers()
            return [0,customers_data]
        if userinfo.internal == '1':
            print(userinfo.fullname +" is servicer")
            # 客服登录成功后，获取所有客户的数据并存储在后端
            customers_data = self.UserRepo.getAllCustomers()
            return [1,customers_data]
