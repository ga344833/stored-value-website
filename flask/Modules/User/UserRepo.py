from OrmModels.DB import session
from Modules.User.Model import User
class UserRepo:
    def __init__(self):
        self.db = session
    
    def create(self , fullname:str , phone:str , email:str , username:str , password:str , gender:str):
        return True

    def getUserByName(self , userName:str)->dict:
        userinfo = self.db.query(User).filter_by(username=userName).first()
        return userinfo