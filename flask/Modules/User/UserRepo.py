from OrmModels.DB import session
from Modules.User.Model import User
import redis
import json
from datetime import datetime
class UserRepo:
    def __init__(self):
        self.db = session
    
    def create(self , fullname:str , phone:str , email:str , username:str , password:str , gender:str , register_time=None):
        new_user = User(fullname=fullname,
        phone=phone,
        email=email,
        username=username,
        password=password,
        gender=gender,
        internal="0",
        register_time=datetime.now())
        self.db.add(new_user)
        self.db.commit()
        return True

    def getUserByName(self , userName:str)->dict:
        userinfo = self.db.query(User).filter_by(username=userName).first()
        return userinfo
    
    def getAllCustomers(self):
        # 获取所有客户的数据
        customers = self.db.query(User).filter_by(internal='0').all()
        # 将客户数据转换为字典列表
        customers_data = [{"id": customer.id, 
                           "fullname": customer.fullname,
                           "phone" : customer.phone,
                           "email": customer.email} for customer in customers]
        return customers_data
    
