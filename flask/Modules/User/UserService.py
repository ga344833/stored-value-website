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
        if userinfo['password'] != dto.passWord:
            raise ValueError("password_no_match")
        
