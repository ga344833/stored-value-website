from .ServicerRepo import ServicerRepo
# from .dtos import registerDto,loginDto

class ServicerService:
    def __init__(self):
        self.ServicerRepo = ServicerRepo()

    def getuserinfo(self):
        print("--2--")
        userinfo = self.ServicerRepo.getUserByName()
        return userinfo

    # def create(self , dto:registerDto):
    #     dto.check()
    #     result = self.UserRepo.create(dto.fullname , dto.phone , dto.email , dto.username , dto.password , dto.gender)
    #     return result

    # # 先依照username找出user 再比對密碼
    # def login(self , dto:loginDto):
    #     dto.check()
    #     userinfo = self.UserRepo.getUserByName(dto.userName)
    #     if userinfo.password != dto.passWord:
    #         return 2
    #     if userinfo.internal == '0':
    #         return 0
    #     if userinfo.internal == '1':
    #         return 1
