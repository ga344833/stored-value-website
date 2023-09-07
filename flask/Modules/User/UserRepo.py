from OrmModels.DB import session

class UserRepo:
    def __init__(self):
        self.db = session
    
    def create(self , fullname:str , phone:str , email:str , username:str , password:str , gender:str):
        return True

    def getUserByName(self , userMame:str)->dict:
        return {"password":"admin"}