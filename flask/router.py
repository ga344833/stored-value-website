from flask import Blueprint
from Modules.User.UserController import UserController
from Modules.Servicer.ServicerController import ServicerController
from Middlewares.JWTMiddleware import JWTMiddleware

allRoute = Blueprint('allRoute', __name__)

@allRoute.post('/users')
def userRegister(): return UserController().create()

@allRoute.post('/login')
def userLogin(): return UserController().login()

@allRoute.post('/perfectinfo')
def PerfectInfo(): return UserController().PerfectInfo()

@allRoute.get('/customers')   ## 不要用 getAllcustomerinfo，All 會讓人誤會是讀取所有信息，但這個api只是獲取客戶信息。而C大寫的意義在於，常量成員命名通常以大寫來識別
@JWTMiddleware.confirm_token  # 添加 JWTMiddleware 装饰器
def getCustomersInfo(): return UserController().getCustomersInfo()

@allRoute.get('/customer/profile')   
@JWTMiddleware.confirm_token  # 添加 JWTMiddleware 装饰器
def get_customer_profile(): return UserController().get_customer_profile()