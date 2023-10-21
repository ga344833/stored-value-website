from flask import Blueprint
from Modules.User.UserController import UserController
from Modules.Servicer.ServicerController import ServicerController
from Middlewares.JWTMiddleware import JWTMiddleware

allRoute = Blueprint('allRoute', __name__)

@allRoute.post('/customer') #創建客戶
def UserRegister(): return UserController().UserRegister()

@allRoute.post('/serivice') #創建客服
def SeriviceRegister(): return UserController().SeriviceRegister()

@allRoute.post('/login') #登入
def userLogin(): return UserController().login()

@allRoute.get('/customers')   #獲取所有客戶資訊
@JWTMiddleware.confirm_token
@JWTMiddleware.check_internal
def getCustomersInfo(): return UserController().getCustomersInfo()

@allRoute.get('/customer/<int:customer_id>')   #獲取指定客戶資訊
@JWTMiddleware.confirm_token
@JWTMiddleware.check_internal  
def getCustomerInfo(customer_id): return UserController().getCustomerInfo(customer_id)

@allRoute.patch('/customer/<int:customer_id>/verify')   #審核指定客戶資訊
@JWTMiddleware.confirm_token
@JWTMiddleware.check_internal 
def verifyCustomer(customer_id): return UserController().verifyCustomer(customer_id)

@allRoute.get('/customer/profile')   #獲取自身客戶資訊
@JWTMiddleware.confirm_token
@JWTMiddleware.get_JWT_userid 
def get_customer_profile(user_id): return UserController().get_customer_profile(user_id)

@allRoute.patch('/customer/profile') #修改客戶資訊
@JWTMiddleware.confirm_token
@JWTMiddleware.get_JWT_userid  
def patch_customer_profile(user_id): return UserController().patch_customer_profile(user_id)

@allRoute.post('/customer/upload_image') # 上傳驗證照片
@JWTMiddleware.confirm_token
@JWTMiddleware.get_JWT_userid 
def upload_image(user_id): return UserController().upload_image(user_id)

### bankcard 

@allRoute.get('/bankcards')   #獲取所有銀行卡資訊
@JWTMiddleware.confirm_token  
def getBankcardsInfo(): return UserController().getBankcardsInfo()

@allRoute.get('/bankcard/profile')   #獲取自身銀行卡資訊
@JWTMiddleware.confirm_token  
def get_bankcard_profile(): return UserController().get_bankcard_profile()

@allRoute.post('/bankcard/create') #創建銀行卡
@JWTMiddleware.confirm_token
def createbankcard(): return UserController().createbankcard()

@allRoute.post('/bankcard/upload_image') # 上傳銀行卡照片
@JWTMiddleware.confirm_token
def upload_bankcard_image(): return UserController().upload_bankcard_image()


@allRoute.get('/bankcard/<int:customer_id>')   #獲取指定客戶銀行卡
@JWTMiddleware.confirm_token  
def getBankcardInfo(customer_id): return UserController().getBankcardInfo(customer_id)

@allRoute.patch('/bankcard/<int:customer_id>/verify')   #審核指定客戶銀行卡
@JWTMiddleware.confirm_token  
def verifyBankcard(customer_id): return UserController().verifyBankcard(customer_id)

## product : 客服 新增商品
@allRoute.post('/product/create') #創建商品
@JWTMiddleware.confirm_token
@JWTMiddleware.check_internal
def createproduct(): return UserController().createproduct()

@allRoute.get('/products')   #獲取所有商品資訊
@JWTMiddleware.confirm_token  
def getproductsInfo(): return UserController().getproductsInfo()

@allRoute.delete('/product/delete') #刪除商品
@JWTMiddleware.confirm_token
@JWTMiddleware.check_internal
def deleteproduct(): return UserController().deleteproduct()

@allRoute.patch('/product/profile') #修改商品資訊
@JWTMiddleware.confirm_token
@JWTMiddleware.check_internal  
def patch_product_profile(): return UserController().patch_product_profile()

## account
@allRoute.post('/account/<int:customer_id>') #創建虛擬帳戶
@JWTMiddleware.confirm_token
@JWTMiddleware.check_internal  
def CreateAccount(customer_id): return UserController().CreateAccount(customer_id)

## 顯示 : get 分別為 客服、客戶 共兩個

@allRoute.get('/account/profile')   #獲取自身帳戶資訊
@JWTMiddleware.confirm_token
@JWTMiddleware.get_JWT_userid  
def get_account_profile(user_id): return UserController().get_account_profile(user_id)

@allRoute.get('/account/<int:customer_id>')   #獲取指定客戶帳戶
@JWTMiddleware.confirm_token
@JWTMiddleware.check_internal  
def getAccountInfo(customer_id): return UserController().getAccountInfo(customer_id)

## 購物流程

@allRoute.post('/purchases/process')   #處理購物流程(1.扣款、扣庫存 2.回傳購物紀錄資訊 給第2隻API做事情)
@JWTMiddleware.confirm_token #前端傳遞的資訊 : 1. customer 2. total 3. product 4. product_amount
@JWTMiddleware.get_JWT_userid 
def ProcessPurchase(user_id): return UserController().ProcessPurchase(user_id) 

@allRoute.post('/purchases/new')   #建立購物紀錄
@JWTMiddleware.confirm_token
@JWTMiddleware.get_JWT_userid
def CreatePurchaseRecord(user_id): return UserController().CreatePurchaseRecord(user_id)

@allRoute.get('/purchases/all')   #客服獲取購物紀錄
@JWTMiddleware.confirm_token
@JWTMiddleware.check_internal 
def GetAllPurchaseRecord(): return UserController().GetAllPurchaseRecord()

@allRoute.get('/purchases')   #客戶獲取購物紀錄
@JWTMiddleware.confirm_token
@JWTMiddleware.get_JWT_userid
def GetPurchaseRecord(user_id): return UserController().GetPurchaseRecord(user_id)

## 儲值 : 
@allRoute.post('/account/create_payment')   #用戶儲值
@JWTMiddleware.confirm_token
@JWTMiddleware.get_JWT_userid  
def Accountdeposit(user_id): return UserController().Accountdeposit(user_id)

@allRoute.post('/account/receive_result')   #處理儲值結果
def Receiveresult(): return UserController().Receiveresult()

@allRoute.get('/account/all_topup_record')   #客服獲取儲值紀錄
@JWTMiddleware.confirm_token
@JWTMiddleware.check_internal   
def getAllTopupRecordsInfo(): return UserController().getAllTopupRecordsInfo()

@allRoute.get('/account/topup_record')   #客戶獲取儲值紀錄
@JWTMiddleware.confirm_token
@JWTMiddleware.get_JWT_userid  
def getTopupRecordsInfo(user_id): return UserController().getTopupRecordsInfo(user_id)


# @allRoute.get('/account/trad_result')   #顯示儲值結果
# def Receiveresult(): return UserController().Receiveresult()

# @allRoute.post('/account/trad_result')   #顯示儲值結果
# def Receiveresult(): return UserController().Receiveresult()

