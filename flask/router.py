from flask import Blueprint
from Modules.User.UserController import UserController
from Modules.Servicer.ServicerController import ServicerController
from Middlewares.JWTMiddleware import JWTMiddleware

allRoute = Blueprint('allRoute', __name__)

@allRoute.post('/users') #創建客戶
def userRegister(): return UserController().create()

@allRoute.post('/login') #登入
def userLogin(): return UserController().login()

@allRoute.get('/customers')   #獲取所有客戶資訊
@JWTMiddleware.confirm_token  
def getCustomersInfo():
    print('--t3--')
    return UserController().getCustomersInfo()

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

@allRoute.get('/bankcard/profile')   #獲取自身銀行卡資訊
@JWTMiddleware.confirm_token  
def get_bankcard_profile(): return UserController().get_bankcard_profile()

@allRoute.post('/bankcard/create') #創建銀行卡
@JWTMiddleware.confirm_token
def createbankcard(): return UserController().createbankcard()

@allRoute.post('/bankcard/upload_image') # 上傳銀行卡照片
@JWTMiddleware.confirm_token
def upload_bankcard_image(): return UserController().upload_bankcard_image()