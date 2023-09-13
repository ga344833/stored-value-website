from flask import Blueprint
from Modules.User.UserController import UserController
from Modules.Servicer.ServicerController import ServicerController
from Middlewares.JWTMiddleware import JWTMiddleware

allRoute = Blueprint('allRoute', __name__)

@allRoute.post('/user')
def userRegister(): return UserController().create()

@allRoute.post('/user/login')
def userLogin(): return UserController().login()

@allRoute.post('/user/userinfo')
def GetUserinfo(): return ServicerController.getUserinfo()