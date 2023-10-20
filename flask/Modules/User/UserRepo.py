from OrmModels.DB import session
from Modules.User.Model import User,Bankcard,Account,Deposit,Product,Purchase_record,Topup_record
import redis
import json
from datetime import datetime
class UserRepo:
    def __init__(self):
        self.db = session
    
    def UserRegister(self , fullname:str , phone:str , email:str , username:str , hashed_password , gender:str ,salt, register_time=None , state=None):
        try:
            check_password = self.db.query(User).filter_by(password=hashed_password).first()
            check_username = self.db.query(User).filter_by(username=username).first()
            if check_password:
                return {"success":False,"message": "password has been used."}
            elif check_username:
                return {"success":False,"message": "username has been used."}
            else:
                new_user = User(fullname=fullname,phone=phone,email=email,username=username,password=hashed_password
                                ,gender=gender,internal="0",salt=salt,register_time=datetime.now(),state="waiting")
                self.db.add(new_user)
                self.db.commit()                
                return {"success":True,
                        "message":str(fullname)+" success create"}
        except:
            return {"success":False,"message": "An error occurred while Create customer data."}

    def SeriviceRegister(self , fullname:str , username:str , hashed_password  ,salt, register_time=None , state=None):
        try:
            check_password = self.db.query(User).filter_by(password=hashed_password).first()
            check_username = self.db.query(User).filter_by(username=username).first()
            if check_password:
                return {"success":False,"message": "password has been used."}
            elif check_username:
                return {"success":False,"message": "username has been used."}
            else:
                new_user = User(fullname=fullname,phone='null',email='null',username=username,password=hashed_password
                                ,gender='null',internal="1",salt=salt,register_time=datetime.now(),state="waiting")
                self.db.add(new_user)
                self.db.commit()                
                return {"success":True,
                        "message":str(fullname)+" success create"}
        except:
            return {"success":False,"message": "An error occurred while Create customer data."}
           
    def getUserByName(self , userName:str)->dict:
        try :            
            userinfo = self.db.query(User).filter_by(username=userName).first()            
            return userinfo
        except Exception as e:
            return {"error": "An error occurred while fetching customer data."}
        
    def getSaltinfo(self , userName:str)->str:
        try :            
            salt = self.db.query(User.salt).filter_by(username=userName).first()            
            return str(salt[0])       
        except Exception as e:
            return {"error": "An error occurred while fetching data."}
    
    def login(self , hashed_password)->dict:
        userinfo = self.db.query(User).filter_by(password=hashed_password).first()   
        try :            
            userinfo = self.db.query(User).filter_by(password=hashed_password).first()            
            return userinfo
        
        except Exception as e:
            return {"error": "An error occurred while fetching data."}
    
    def getCustomersInfo(self): 
        try :
            customers = self.db.query(User).filter_by(internal='0').all()
            customers_data = [{"id": customer.id,             
                            "fullname": customer.fullname,
                            "phone" : customer.phone,
                            "email": customer.email,
                            "register_time":customer.register_time,
                            "state":customer.state} for customer in customers]
            customers_wainting_data = [{"id": customer.id,             
                            "fullname": customer.fullname,
                            "phone" : customer.phone,
                            "email": customer.email,
                            "register_time":customer.register_time,
                            "state":customer.state} for customer in customers if customer.state == 'waiting']
            return customers_data,customers_wainting_data
        except Exception as e:
            return {"error": "An error occurred while fetching customer data."}
    
    def getBankcardsInfo(self): 
        try :
            bankcards = self.db.query(Bankcard).all()
            bankcards_data = [{"id": bankcard.id,             
                            "user_id": bankcard.user_id,
                            "bank" : bankcard.bank,
                            "card_number": bankcard.card_number,
                            "state":bankcard.state} for bankcard in bankcards]
            bankcards_waiting_data = [{"id": bankcard.id,             
                            "user_id": bankcard.user_id,
                            "bank" : bankcard.bank,
                            "card_number": bankcard.card_number,
                            "state":bankcard.state} for bankcard in bankcards if bankcard.state == 'waiting']
            
            return bankcards_data,bankcards_waiting_data
        except Exception as e:
            return {"error": "An error occurred while fetching customer data."}
    
    def getCustomerById(self,customer_id):
        try:
            customer = self.db.query(User).filter_by(id=customer_id).first()
            return customer
        except Exception as e:
            return {"error": "An error occurred while fetching customer data. :"}
        
    def getBankcardById(self,customer_id):
        try:
            bankcard = self.db.query(Bankcard).filter_by(user_id=customer_id).first()
            return bankcard
        except Exception as e:
            return {"error": "An error occurred while fetching customer data. :"}
        
    def verifyCustomer(self,customer_id:int,state:str):
        try:
            customer = self.db.query(User).filter_by(id=customer_id).first()
            if not customer:
                return {'success': False, 'message': 'Customer not found'}
            customer.state = state
            self.db.commit()
            return customer
        except Exception as e:
            return {"error": "An error occurred while fetching customer data. :"}

    def patchCustomerInfo(self, customer_id:int , country:str ,idtype:str,idnumber:str):
        try:
            customer = self.db.query(User).filter_by(id=customer_id).first()
            if not customer:
                return {'success': False, 'message': 'Customer not found'}
            customer.country = country
            customer.idtype = idtype
            customer.idnumber = idnumber
            customer.state = "waiting"
            self.db.commit()
            return {'success': True, 'message': 'Success updating customer info'}
        except Exception as e:
            print(e)
            return {"error": "An error occurred"}

    def patchProductInfo(self,product_id:int, name:str, price:int ,amount:int): ## 前端輸入前、綁定原始資料
        try:
            product = self.db.query(Product).filter_by(id=product_id).first()
            if not product:
                return {'success': False, 'message': 'Product not found'}
            product.price = price
            product.name = name
            product.amount = amount
            product.date_modified=datetime.now()
            self.db.commit()
            return {'success': True, 'message': 'Success updating product info'}
        except Exception as e:
            print(e)
            return {"error": "An error occurred,plz check python"}

         
    def uploadInfo(self,customer_id:int,file:bytes):
        try:
            customer = self.db.query(User).filter_by(id=customer_id).first()
            if not customer:
                return {'success': False, 'message': 'Customer not found'}
            image_data = file.read()
            file.seek(0)
            customer.profile_image = image_data
            self.db.commit()
            return {'success': True, 'message': 'Success updated customer info'}
        except Exception as e:
            print(e)
            return {"error": "An error occurred,plz check python"}
        
    def uploadBankcardInfo(self,customer_id:int,file:bytes):
        try:
            bankcard = self.db.query(Bankcard).filter_by(user_id=customer_id).first()
            if not bankcard:
                return {'success': False, 'message': 'bankcard not found'}
            image_data = file.read()
            file.seek(0)
            bankcard.card_image = image_data
            self.db.commit()
            return {'success': True, 'message': 'Success updated bankcard info'}
        except Exception as e:
            print(e)
            return {"error": "An error occurred,plz check python"}

    def createbankcard(self , customer_id:int,card_number:str,bank:str):
        try:
            bankcard = self.db.query(Bankcard).filter_by(user_id=customer_id).first()
            if bankcard:
                return {'success': False, 'message': "already have bankcard"}
            bankcard = Bankcard(user_id=customer_id,card_number=card_number,state='waiting',bank=bank)
            self.db.add(bankcard)
            self.db.commit()
            return {'success': True, 'message': 'Success updated bankcard info'}
        except Exception as e:
            print(e)
            return {'success': False, 'message': "Fail to updated bankcard,plz check SQL"}
    

    def verifyBankcard(self,customer_id:int,state:str):
        try:
            bankcard = self.db.query(Bankcard).filter_by(user_id=customer_id).first()
            if not bankcard:
                return {'success': False, 'message': 'Bankcard not found'}
            bankcard.state = state
            self.db.commit()
            return bankcard
        except Exception as e:
            return {"error": "An error occurred while fetching customer data. :"}

    def CreateAccount(self ,customer_id:int,balance:int,account_number:str):
        print("--2--")
        try:
            ## check user state
            print(customer_id)
            userinfo = self.db.query(User).filter_by(id=customer_id).first()
            print(userinfo)
            if userinfo.state != "approved":
                return {'success': False, 'message': "user state not approved"}
            print("--3--")
            account = self.db.query(Account).filter_by(user_idnumber=userinfo.idnumber).first()
            if account:
                return {'success': False, 'message': "already have account"}
            print("--4--")
            account = Account(user=userinfo.fullname,user_idnumber=userinfo.idnumber,account_number=account_number,balance=balance,state="unforzen")
            self.db.add(account)
            self.db.commit()
            return {'success': True, 'message': 'Success updated account info'}
        except Exception as e:
            print(e)
            return {'success': False, 'message': "Fail to updated account,plz check SQL"}
    
    def getAccountById(self,customer_id):
        try:
            userinfo = self.db.query(User).filter_by(id=customer_id).first()
            account = self.db.query(Account).filter_by(user_idnumber=userinfo.idnumber).first()
            return account
        except Exception as e:
            return {"error": "An error occurred while fetching customer data. :"}

    def getPurchaseRecordsById(self,customer_id):
        try:
            userinfo = self.db.query(User).filter_by(id=customer_id).first()
            purchase_records = self.db.query(Purchase_record).filter_by(buyer=userinfo.fullname).all()
            purchase_record_data = [{"id":purchase_record.id,
                "buyer":purchase_record.buyer,
                "purchase_time":purchase_record.purchase_time,
                "product_item":purchase_record.product_item,
                "item_id":purchase_record.item_id,
                "product_amount":purchase_record.product_amount,
                "total":purchase_record.total,
                "buyer_balance":purchase_record.buyer_balance,
                "after_purchase_balance":purchase_record.after_purchase_balance} for purchase_record in purchase_records]
            return purchase_record_data
        except Exception as e:
            return {"error": "An error occurred while fetching customer data. :"}
        
    def getAllPurchaseRecordsById(self,customer_id):
        try:
            purchase_records = self.db.query(Purchase_record).all()
            purchase_record_data = [{"id":purchase_record.id,
                "buyer":purchase_record.buyer,
                "purchase_time":purchase_record.purchase_time,
                "product_item":purchase_record.product_item,
                "item_id":purchase_record.item_id,
                "product_amount":purchase_record.product_amount,
                "total":purchase_record.total,
                "buyer_balance":purchase_record.buyer_balance,
                "after_purchase_balance":purchase_record.after_purchase_balance} for purchase_record in purchase_records]
            return purchase_record_data
        except Exception as e:
            return {"error": "An error occurred while fetching customer data. :"}

    
    def TopupSuccessRecord(self , amount  , customername , account_number , user_balance):
        try:
            record = Topup_record(user=customername,
                                  account_number=account_number,
                                  topup_balance=amount,
                                  topup_time=datetime.now(),
                                  user_balance=user_balance)
            self.db.add(record)
            self.db.commit()
            return {'success': True, 'message': 'Success updated Deposit info'}
        except Exception as e:
            print(e)
            return {'success': False, 'message': "Fail to updated account,plz check SQL"}
 
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

    def createproduct(self , name:str,price:int,amount:int):
        try:
            product = self.db.query(Product).filter_by(name=name).first()
            if product:
                return {'success': False, 'message': "already have product"}
            product = Product(name=name,price=price,amount=amount,date_add=datetime.now(),date_modified=datetime.now())
            self.db.add(product)
            self.db.commit()
            return {'success': True, 'message': 'Success updated product'}
        except Exception as e:
            print(e)
            return {'success': False, 'message': "Fail to updated product,plz check SQL"}
    
    def deleteproduct(self , name:str):
        try:
            product = self.db.query(Product).filter_by(name=name).first()
            if product:
                self.db.delete(product)
                self.db.commit()
                return {'success': True, 'message': 'Success delete product'}
            else:
                return {'success': False, 'message': "do not have this product"}
        except Exception as e:
            print(e)
            return {'success': False, 'message': "Fail to delete product,plz check SQL"}

    

    def getproductsInfo(self): 
        try :
            products = self.db.query(Product).all()
            products_data = [{"id": product.id,             
                            "name": product.name,
                            "price" : product.price,
                            "amount": product.amount,
                            "image":product.image,
                            "date_add":product.date_add,
                            "date_modified":product.date_modified} for product in products]
            
            return products_data
        except Exception as e:
            return {"error": "An error occurred while fetching customer data."}
        
    def getAllTopupRecordsInfo(self): 
        try :
            topup_records = self.db.query(Topup_record).all()
            topup_records_data = [{"id": topup_record.id,             
                            "user": topup_record.user,
                            "account_number" : topup_record.account_number,
                            "topup_balance": topup_record.topup_balance,
                            "topup_time":topup_record.topup_time,
                            "user_balance":topup_record.user_balance
                            } for topup_record in topup_records]            
            return topup_records_data
        except Exception as e:
            return {"error": "An error occurred while fetching customer data."}
        
    def getTopupRecordsInfo(self,username): 
        try :
            topup_records = self.db.query(Topup_record).filter_by(user=username).all()
            topup_records_data = [{"id": topup_record.id,             
                            "user": topup_record.user,
                            "account_number" : topup_record.account_number,
                            "topup_balance": topup_record.topup_balance,
                            "topup_time":topup_record.topup_time,
                            "user_balance":topup_record.user_balance
                            } for topup_record in topup_records]            
            return topup_records_data
        except Exception as e:
            return {"error": "An error occurred while fetching customer data."}
        
    def CreatePurchaseRecord(self ,customer_id:int,buyer:str,product_item:str,item_id:int,product_amount:int,total:int,buyer_balance:int,after_purchase_balance:int):
        try:
            purchase_record = Purchase_record(buyer=buyer,
                                     product_item=product_item,
                                      item_id=item_id,
                                      product_amount=product_amount,
                                      total=total,
                                      buyer_balance=buyer_balance,
                                      after_purchase_balance=after_purchase_balance,
                                      purchase_time=datetime.now())
            self.db.add(purchase_record)
            self.db.commit()
            return {'success': True, 'message': 'Success instert purchase_record'}
        except Exception as e:
            print(e)
            return {'success': False, 'message': "Fail to instert purchase_record,plz check SQL"}
   
    def ProcessPurchase(self ,useraccount,productinfo):
        try:            
            self.db.add(useraccount)
            self.db.commit()
            self.db.add(productinfo)
            self.db.commit()
            return {'success': True, 'message': 'Success change useraccount&productinfo'}
        except Exception as e:
            print(e)
            return {'success': False, 'message': "Fail to change useraccount&productinfo,plz check SQL"}
   
    def AddCustomerBalance(self ,Account):
        try:            
            self.db.add(Account)
            self.db.commit()
            return {'success': True, 'message': 'Success Add Balance'}
        except Exception as e:
            print(e)
            return {'success': False, 'message': "Fail to Add Balance,plz check SQL"}
   

    def getproductInfo(self,product_item:str): 
        try :
            product = self.db.query(Product).filter_by(name=product_item).first()   
            return product
        except Exception as e:
            return {"error": "An error occurred while fetching product."}
