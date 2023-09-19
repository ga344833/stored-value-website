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
        try :
            userinfo = self.db.query(User).filter_by(username=userName).first()
            return userinfo
        except Exception as e:
            return {"error": "An error occurred while fetching customer data."}
    
    def getCustomersInfo(self): 
        try :
            customers = self.db.query(User).filter_by(internal='0').all()
            customers_data = [{"id": customer.id,             
                            "fullname": customer.fullname,
                            "phone" : customer.phone,
                            "email": customer.email} for customer in customers]
            return customers_data
        except Exception as e:
            return {"error": "An error occurred while fetching customer data."}
    
    def getCustomerById(self,customer_id):
        try:
            customer = self.db.query(User).filter_by(id=customer_id).first()
            return customer
        except Exception as e:
            return {"error": "An error occurred while fetching customer data."}
        
    def patchCustomerInfo(self, customer_id:int , country:str ,idtype:str,idnumber:str):
        try:
            customer = self.db.query(User).filter_by(id=customer_id).first()
            if not customer:
                return {'success': False, 'message': 'Customer not found'}
            customer.country = country
            customer.idtype = idtype
            customer.idnumber = idnumber
            self.db.commit()
            return {'success': True, 'message': 'Success updating customer info'}
        except Exception as e:
            print(e)
            return {"error": "An error occurred"}
        
    def uploadInfo(self,customer_id:int,file:bytes):
        try:
            customer = self.db.query(User).filter_by(id=customer_id).first()
            if not customer:
                return {'success': False, 'message': 'Customer not found'}
            image_data = file.read()
            file.seek(0)
            print(image_data)
            customer.profile_image = image_data
            self.db.commit()
            return {'success': True, 'message': 'Success updating customer info'}
        except Exception as e:
            print(e)
            return {"error": "An error occurred"}

        
    # def perfectInfo(self,country:str ,ID_type:str,ID_number:str,profile_image:str):
    #     user = 
        
    
    # def cache_customers_data(self,customer_data):
    #     try:
    #         redis_host = "localhost"
    #         redis_port = 6379
    #         redis_password = "yu023468"
    #         r = redis.StrictRedis(host=redis_host,
    #                               port=redis_port,
    #                               password=redis_password)
    #         for customer in customer_data:
    #             if not r.hexists('customer',customer["id"]):
    #                 data_to_store = str(customer["id"]) + json.dumps(customer)
    #                 r.hset("customers",str(customer["id"]),data_to_store)
    #                 print(customer)
    #     except Exception as e:
    #         print("Error caching customer data:",str(e))