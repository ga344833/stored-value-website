from .UserRepo import UserRepo
from .dtos import registerDto,loginDto,perfectInfoDto,ImageDto,VerifyCustomerDto,CreateBankcardDto,VerifyBankcardDto,CreateAccountDto,CreateProductDto,DeleteProductDto,PatchProductDto,CreatePurchaseRecordDto,ProcessPurchaseDto
import jwt
from datetime import datetime, timedelta
import base64
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
        print(userinfo.password)
        if userinfo.password != dto.passWord:
            return [userinfo,2]
        if userinfo.internal == '0': 
            return [userinfo,0]
        if userinfo.internal == '1':
            print(userinfo.fullname +" is servicer")
            return [userinfo,1]
    
    def getCustomersInfo(self):
        CustomersInfo = self.UserRepo.getCustomersInfo()
        return CustomersInfo
    
    def getBankcardsInfo(self):
        BankcardsInfo = self.UserRepo.getBankcardsInfo()
        return BankcardsInfo

    def getproductsInfo(self):
        ProductsInfo = self.UserRepo.getproductsInfo()
        return ProductsInfo

    def patchCustomerInfo(self,dto:perfectInfoDto):
        dto.check()
        result = self.UserRepo.patchCustomerInfo(dto.customer_id , dto.country , dto.idtype , dto.idnumber)
        return result
    
    def patchProductInfo(self,dto:PatchProductDto):
        dto.check()
        result = self.UserRepo.patchProductInfo(dto.product_id,dto.name , dto.price , dto.amount)
        return result
    
    def uploadInfo(self,dto:ImageDto):
        dto.check()
        result = self.UserRepo.uploadInfo(dto.customer_id , dto.file)
        return result
    
    def uploadBankcardInfo(self,dto:ImageDto):
        dto.check()
        result = self.UserRepo.uploadBankcardInfo(dto.customer_id , dto.file)
        return result

    def getCustomerById(self, customer_id):
        customer = self.UserRepo.getCustomerById(customer_id)
        try:
            customer_info = {
                'id' : customer.id,
                'fullname': '',
                'phone': '',
                'email': '',
                'country': '',
                'username':'',
                'password':'',
                'idtype': '',
                'idnumber': '',
                'forzen':'',
                'gender':'',
                'profile_image':'',
                'state':'',
                'register_time':''
                }
            if customer:
                customer_info['fullname'] = customer.fullname
                customer_info['phone'] = customer.phone
                customer_info['email'] = customer.email
                if 'country' in customer.__dict__:
                    customer_info['country'] = customer.country
                if 'username' in customer.__dict__:
                    customer_info['username'] = customer.username
                if 'password' in customer.__dict__:
                    customer_info['password'] = customer.password
                if 'idtype' in customer.__dict__:
                    customer_info['idtype'] = customer.idtype
                if 'idnumber' in customer.__dict__:
                    customer_info['idnumber'] = customer.idnumber
                if 'profile_image' in customer.__dict__:
                    try:
                        i2 = customer.profile_image
                        img = base64.b64encode(customer.profile_image).decode("utf-8")
                        customer_info['profile_image'] = img
                    except:
                        pass
                if 'forzen' in customer.__dict__:
                    customer_info['forzen'] = customer.forzen
                if 'gender' in customer.__dict__:
                    customer_info['gender'] = customer.gender
                if 'state' in customer.__dict__:
                    customer_info['state'] = customer.state
                if 'register_time' in customer.__dict__:
                    customer_info['register_time'] = customer.register_time
            
            return customer_info
        except:
            customer_info = {
                'id' : "",
                'fullname': '',
                'phone': '',
                'email': '',
                'country': '',
                'username':'',
                'password':'',
                'idtype': '',
                'idnumber': '',
                'forzen':'',
                'gender':'',
                'profile_image':'',
                'state':'',
                'register_time':''
                }
            return customer_info
    def getBankcardById(self, customer_id):
        BankcardsInfo = self.UserRepo.getBankcardById(customer_id)
        try:
            bankcard_info = {
                'id' : BankcardsInfo.id,
                'user_id': '',
                'bank': '',
                'card_number': '',
                'card_image': '',
                'state': ''
                }
            if 'user_id' in BankcardsInfo.__dict__:
                bankcard_info['user_id'] = BankcardsInfo.user_id
            if 'bank' in BankcardsInfo.__dict__:
                bankcard_info['bank'] = BankcardsInfo.bank
            if 'card_number' in BankcardsInfo.__dict__:
                bankcard_info['card_number'] = BankcardsInfo.card_number
            if 'state' in BankcardsInfo.__dict__:
                bankcard_info['state'] = BankcardsInfo.state
            if 'card_image' in BankcardsInfo.__dict__:
                try:
                    img = base64.b64encode(BankcardsInfo.card_image).decode("utf-8")
                    bankcard_info['card_image'] = img
                except:
                    pass
            return bankcard_info
        except:
            bankcard_info = {
                'id' : '',
                'user_id': '',
                'bank': '',
                'card_number': '',
                'card_image': '',
                'state': ''
                }
            return bankcard_info
    
    def verifyCustomer(self, dto:VerifyCustomerDto):
        dto.check()
        customer = self.UserRepo.verifyCustomer(dto.customer_id,dto.state)
        return customer
    
    # 生成 JWT 令牌
    def generate_token(self,user):
        payload = {
            'sub' : user.id,
            'exp' : datetime.utcnow() + timedelta(days=1),
            'iat' : datetime.utcnow()
        }
        token = jwt.encode(payload,'yu023468',algorithm='HS256')
        return token
    
    def perfectInfo(self,dto:perfectInfoDto):
        dto.check()
        result = self.UserRepo.perfectInfo(dto.country , dto.ID_type , dto.ID_number , dto.profile_image)
        return result
    
    def createbankcard(self , dto:CreateBankcardDto):
        dto.check()
        result = self.UserRepo.createbankcard(dto.customer_id , dto.card_number , dto.bank)
        return result ## {'success': True, 'message': 'Success updated bankcard info'}

    def createproduct(self , dto:CreateProductDto):
        dto.check()
        result = self.UserRepo.createproduct(dto.name , dto.price , dto.amount)
        return result ## {'success': True, 'message': 'Success updated bankcard info'}

    def deleteproduct(self , dto:DeleteProductDto):
        dto.check()
        result = self.UserRepo.deleteproduct(dto.name)
        return result ## {'success': True, 'message': 'Success updated bankcard info'}


    def verifyBankcard(self, dto:VerifyBankcardDto):
        dto.check()
        customer = self.UserRepo.verifyBankcard(dto.customer_id,dto.state)
        return customer
    
    def CreateAccount(self,dto:CreateAccountDto):
        dto.check()
        account = self.UserRepo.CreateAccount(dto.customer_id,dto.balance,dto.account_number)
        return account
    
    def CreatePurchaseRecord(self,dto:CreatePurchaseRecordDto):
        dto.check()
        PurchaseRecord = self.UserRepo.CreatePurchaseRecord(dto.customer_id,
                                                            dto.buyer,
                                                            dto.product_item,dto.item_id,
                                                            dto.product_amount,dto.total
                                                            ,dto.buyer_balance,
                                                            dto.after_purchase_balance)
        return PurchaseRecord
    
    def ProcessPurchase(self,dto:ProcessPurchaseDto):
        dto.check()
        useraccount = self.UserRepo.getAccountById(dto.customer_id)
        productinfo = self.UserRepo.getproductInfo(dto.product_item)

        buyer_balance = useraccount.balance
        after_purchase_balance = useraccount.balance - dto.total

        product_stock = productinfo.amount - dto.product_amount

        useraccount.balance = after_purchase_balance
        productinfo.amount = product_stock

        ProcessPurchase = self.UserRepo.ProcessPurchase(useraccount,productinfo)
        if ProcessPurchase['success'] == True:
            purchase_record = {'buyer':useraccount.user,
                               "product_item":productinfo.name,
                               "item_id":productinfo.id,
                               "product_amount":dto.product_amount,
                               "total":dto.total,
                               "buyer_balance":buyer_balance,
                               "after_purchase_balance":after_purchase_balance}
        
        return purchase_record

    def getAccountById(self, customer_id):
        Account = self.UserRepo.getAccountById(customer_id)
        try:
            Account_info = {
                'id' : Account.id,
                'user': '',
                'user_idnumber': '',
                'balance': '',
                'account_number': '',
                'state': ''
                }
            if 'user' in Account.__dict__:
                Account_info['user'] = Account.user
            if 'user_idnumber' in Account.__dict__:
                Account_info['user_idnumber'] = Account.user_idnumber
            if 'balance' in Account.__dict__:
                Account_info['balance'] = Account.balance
            if 'account_number' in Account.__dict__:
                Account_info['account_number'] = Account.account_number
            if 'state' in Account.__dict__:
                Account_info['state'] = Account.state
            return Account_info
        except:
            Account_info = {
                'id' : '',
                'user': '',
                'user_idnumber': '',
                'balance': '',
                'account_number': '',
                'state': ''
                }
            return Account_info
    
    def CreateBalanceDeposit(self,dto:CreateAccountDto):
        dto.check()
        account = self.UserRepo.CreateBalanceDeposit(dto.customer_id,dto.account_number,dto.balance,dto.remark)
        return account

    def getPurchaseRecordsById(self, customer_id):
        if customer_id != 1:
            PurchaseRecords = self.UserRepo.getPurchaseRecordsById(customer_id)
            return PurchaseRecords
        if customer_id == 1:
            PurchaseRecords = self.UserRepo.getAllPurchaseRecordsById(customer_id)
            return PurchaseRecords
    