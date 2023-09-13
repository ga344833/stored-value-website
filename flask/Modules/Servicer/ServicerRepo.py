from OrmModels.DB import session
from Modules.Servicer.Model import User
from sqlalchemy import desc
class ServicerRepo:
    def __init__(self):
        self.db = session
    
    # def create(self , fullname:str , phone:str , email:str , username:str , password:str , gender:str):
    #     new_user = User(fullname=fullname,
    #     phone=phone,
    #     email=email,
    #     username=username,
    #     password=password,
    #     gender=gender,
    #     internal="0")
    #     self.db.add(new_user)
    #     self.db.commit()
    #     return True

    def getUserByName(self , userName:str)->dict:
        print("--3--")
        userinfo = self.db.query(User).order_by(desc(User.register_time)).all()
        return userinfo