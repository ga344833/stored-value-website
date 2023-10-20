from  abc import abstractmethod

class dto:
    @abstractmethod
    def check():
        return 

class loginDto():
    def __init__(self , userName:str , passWord:str):
        self.userName = userName
        self.passWord = passWord
    def check(self):
        if self.userName == "":
            raise ValueError('user_name required')
        if self.passWord == "":
            raise ValueError('pass_word required')

class registerDto():
    def __init__(self , fullname:str , phone:str , email:str , username:str , password:str , gender:str):
        self.fullname = fullname
        self.phone = phone
        self.email = email
        self.username = username
        self.password = password
        self.gender = gender
    
    def check(self):
        # 簡易檢查:
        # if "@" not in self.email:
        #     raise ValueError('email Format does not match')
            
        # if 10 != len(self.phone):
        #     raise ValueError('phone Format does not match')
            
        # if 8 > len(self.username):
        #     raise ValueError('username length does not match')
            
        # if 8 > len(self.password):
        #     raise ValueError('password length does not match')
            
        # if self.fullname == None:
        #     raise ValueError('need fullname')

        # if self.gender == None:
        #     raise ValueError('need gender')
        print("--2--")

class perfectInfoDto():
    def __init__(self , customer_id:int , country:str , idtype:str , idnumber:str):
        self.customer_id = customer_id
        self.country = country
        self.idtype = idtype
        self.idnumber = idnumber
    def check(self):
        if self.idtype == "":
            raise ValueError('ID_type required')
        if self.idnumber == "":
            raise ValueError('ID_number required')

class ImageDto():
    def __init__(self ,customer_id:int, file:bytes):
        self.customer_id = customer_id
        self.file = file
        
    def check(self):
        if self.file == "":
            raise ValueError('No selected file')
        
class VerifyCustomerDto():
    def __init__(self ,customer_id:int, state:str):
        self.customer_id = customer_id
        self.state = state
    def check(self):
        if self.state == "":
            raise ValueError('No selected state')
        
class CreateBankcardDto():
    def __init__(self ,customer_id:int, card_number:str , bank:str):
        self.customer_id = customer_id
        self.card_number = card_number
        self.bank = bank
    def check(self):
        # 簡易檢查: 
        if 11 > len(self.card_number):
            raise ValueError('card_number length does not match')
        
class CreateProductDto():
    def __init__(self ,name:str, price:int, amount:int):
        self.name = name
        self.price = price
        self.amount = amount  
    def check(self):
        if self.name == "":
            raise ValueError('need product name')
        
class PatchProductDto():
    def __init__(self ,product_id:int,name:str, price:int, amount:int):
        self.product_id = product_id   
        self.name = name
        self.price = price
        self.amount = amount
    def check(self):
        if self.name == "" and self.price == "" and self.amount == "":
            raise ValueError('need insert')
        
class DeleteProductDto():
    def __init__(self ,name:str):
        self.name = name 
    def check(self):
        if self.name == "":
            raise ValueError('need product name')
            
class VerifyBankcardDto():
    def __init__(self ,customer_id:int, state:str):
        self.customer_id = customer_id
        self.state = state
    def check(self):
        if self.state == "":
            raise ValueError('No selected state')
  
class CreateAccountDto():
    def __init__(self,customer_id,balance,account_number):       
        self.customer_id = customer_id
        self.balance = balance
        self.account_number = account_number
    def check(self):
        print("--1--")
        if self.customer_id == "":
            raise ValueError('No customer_id')
        
class ReceiveresultDto():
    def __init__(self,amount,customer_id,customername,account_number):
        self.amount = amount        
        self.customer_id = customer_id
        self.customername = customername
        self.account_number = account_number
    def check(self):
        print("--1--")
        if self.customer_id == "":
            raise ValueError('No customer_id')

class CreatePurchaseRecordDto():
    def __init__(self,customer_id:int,buyer:str,product_item:str,item_id:int,product_amount:int,total:int,buyer_balance:int,after_purchase_balance:int):
        self.customer_id = customer_id
        self.buyer = buyer
        self.product_item = product_item
        self.item_id = item_id
        self.product_amount = product_amount
        self.total = total
        self.buyer_balance = buyer_balance
        self.after_purchase_balance = after_purchase_balance
    def check(self):
        print("--2--")
        if self.customer_id == "":
            raise ValueError('No customer_id')
        
class ProcessPurchaseDto():
    def __init__(self,customer_id:int,product_item:str,product_amount:int,total:int):
        self.customer_id = customer_id
        self.product_item = product_item
        self.product_amount = product_amount
        self.total = total
    def check(self):
        print("--2--")
        if self.customer_id == "":
            raise ValueError('No customer_id')
        
