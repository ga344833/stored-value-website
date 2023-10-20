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
def getCustomersInfo(): return UserController().getCustomersInfo()

@allRoute.get('/customer/<int:customer_id>')   #獲取指定客戶資訊
@JWTMiddleware.confirm_token  
def getCustomerInfo(customer_id): return UserController().getCustomerInfo(customer_id)

@allRoute.patch('/customer/<int:customer_id>/verify')   #審核指定客戶資訊
@JWTMiddleware.confirm_token  
def verifyCustomer(customer_id): return UserController().verifyCustomer(customer_id)

@allRoute.get('/customer/profile')   #獲取自身客戶資訊
@JWTMiddleware.confirm_token  
def get_customer_profile(): return UserController().get_customer_profile()

@allRoute.patch('/customer/profile') #修改客戶資訊
@JWTMiddleware.confirm_token  
def patch_customer_profile(): return UserController().patch_customer_profile()

@allRoute.post('/customer/upload_image') # 上傳驗證照片
@JWTMiddleware.confirm_token
def upload_image(): return UserController().upload_image()

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
def createproduct(): return UserController().createproduct()

@allRoute.get('/products')   #獲取所有商品資訊
@JWTMiddleware.confirm_token  
def getproductsInfo(): return UserController().getproductsInfo()

@allRoute.delete('/product/delete') #刪除商品
@JWTMiddleware.confirm_token
def deleteproduct(): return UserController().deleteproduct()

@allRoute.patch('/product/profile') #修改商品資訊
@JWTMiddleware.confirm_token  
def patch_product_profile(): return UserController().patch_product_profile()

## account
@allRoute.post('/account/<int:customer_id>') #創建虛擬帳戶
@JWTMiddleware.confirm_token 
def CreateAccount(customer_id): return UserController().CreateAccount(customer_id)

## 顯示 : get 分別為 客服、客戶 共兩個

@allRoute.get('/account/profile')   #獲取自身帳戶資訊
@JWTMiddleware.confirm_token  
def get_account_profile(): return UserController().get_account_profile()

@allRoute.get('/account/<int:customer_id>')   #獲取指定客戶帳戶
@JWTMiddleware.confirm_token  
def getAccountInfo(customer_id): return UserController().getAccountInfo(customer_id)

## 購物流程

@allRoute.post('/purchases/process')   #處理購物流程(1.扣款、扣庫存 2.回傳購物紀錄資訊 給第2隻API做事情)
@JWTMiddleware.confirm_token #前端傳遞的資訊 : 1. customer 2. total 3. product 4. product_amount
def ProcessPurchase(): return UserController().ProcessPurchase() 

@allRoute.post('/purchases/new')   #建立購物紀錄
@JWTMiddleware.confirm_token 
def CreatePurchaseRecord(): return UserController().CreatePurchaseRecord()

@allRoute.get('/purchases')   #獲取購物紀錄
@JWTMiddleware.confirm_token 
def GetPurchaseRecord(): return UserController().GetPurchaseRecord()

## 儲值 : 
@allRoute.post('/account/create_payment')   #用戶儲值
@JWTMiddleware.confirm_token  
def Accountdeposit(): return UserController().Accountdeposit()

@allRoute.post('/account/receive_result')   #處理儲值結果
def Receiveresult(): return UserController().Receiveresult()

@allRoute.get('/account/topup_record')   #獲取儲值紀錄
@JWTMiddleware.confirm_token  
def getTopupRecordsInfo(): return UserController().getTopupRecordsInfo()


# @allRoute.get('/account/trad_result')   #顯示儲值結果
# def Receiveresult(): return UserController().Receiveresult()

# @allRoute.post('/account/trad_result')   #顯示儲值結果
# def Receiveresult(): return UserController().Receiveresult()

