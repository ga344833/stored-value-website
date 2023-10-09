from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,DateTime,LargeBinary, BLOB
from marshmallow import Schema, fields

Base = declarative_base()

class UserSchema(Schema):
    id = fields.Integer()
    fullname = fields.String()
    phone = fields.String()
    email = fields.String()
    country = fields.String()
    idtype = fields.String()
    idnumber = fields.String()
    username = fields.String()
    password = fields.String()
    gender = fields.String()
    internal = fields.String()
    register_time = fields.DateTime()
    profile_image = fields.String()
    state = fields.String()

class User(Base):
    
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    fullname = Column(String(80), unique=True, nullable=False)
    phone = Column(String(80), unique=True, nullable=False)
    email = Column(String(80), unique=True, nullable=False)
    country = Column(String(80), nullable=True)  # 允许为空
    idtype = Column(String(80), nullable=True)
    idnumber = Column(String(80), nullable=True)
    username = Column(String(80), unique=True, nullable=False)
    password = Column(String(80), unique=True, nullable=False)
    gender = Column(String(1), unique=True, nullable=False)
    internal = Column(String(1), unique=True, nullable=False)
    register_time = Column(DateTime(0), unique=True, nullable=False)
    profile_image = Column(BLOB, nullable=True)
    state = Column(String(80), unique=True, nullable=False)

    def __init__(self , fullname:str , phone:str , email:str , username:str, password:str , gender:str , internal:str , register_time:None
                 ,country=None, idtype=None, idnumber=None, profile_image=None,state=None):
        self.fullname = fullname
        self.phone = phone
        self.email = email
        self.username = username
        self.password = password
        self.gender = gender
        self.internal = internal
        self.register_time = register_time
        self.country = country  # 新添加的字段
        self.idtype = idtype  # 新添加的字段
        self.idnumber = idnumber  # 新添加的字段
        self.profile_image = profile_image  # 新添加的字段
        self.state = state
    
    def serialize(self):
        user_schema = UserSchema()
        return user_schema.dump(self)
    
class Bankcard(Base):
    
    __tablename__ = 'bankcard'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, unique=True, nullable=False)
    card_number = Column(String(80), unique=True, nullable=False)
    card_image = Column(BLOB, nullable=True)
    state = Column(String(80), unique=True, nullable=False)
    bank = Column(String(80), unique=True, nullable=False)

    def __init__(self , user_id:int , card_number:str , state:str ,bank:str, pcard_image=None):
        self.user_id = user_id
        self.card_number = card_number
        self.card_image = pcard_image  # 新添加的字段
        self.state = state
        self.bank = bank

class Account(Base):
    
    __tablename__ = 'account'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user = Column(String(80), unique=True, nullable=False)
    user_idnumber = Column(String(80), nullable=True)
    account_number = Column(String(80), unique=True, nullable=False)
    balance = Column(Integer, nullable=True)
    state = Column(String(80), nullable=False)

    def __init__(self , user:str ,user_idnumber:str, account_number:str , balance:int ,state:str):
        self.user = user
        self.user_idnumber = user_idnumber
        self.account_number = account_number
        self.balance = balance  # 新添加的字段
        self.state = state

class Deposit(Base):
    
    __tablename__ = 'customer_balance_deposit'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, unique=True, nullable=False)
    account_id = Column(Integer, unique=True, nullable=False)
    account_number = Column(String(80), unique=True, nullable=False)
    amount = Column(Integer, nullable=True)
    payment_time = Column(DateTime(0), unique=True, nullable=False)
    pay_metnod = Column(String(80), unique=True, nullable=False)
    state = Column(String(80), unique=True, nullable=False)
    remark = Column(String(80), unique=True, nullable=False)

    def __init__(self , user_id:int ,account_id:int, account_number:str , amount:int ,state:str,remark:str,payment_time=None):
        self.user_id = user_id
        self.account_id = account_id
        self.account_number = account_number
        self.amount = amount
        self.state = state
        self.payment_time = payment_time
        self.remark = remark

class Product(Base):
    
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80), unique=True, nullable=False)
    price = Column(Integer, nullable=False)
    amount = Column(Integer, unique=True, nullable=False)
    date_add = Column(DateTime(0), unique=True, nullable=False)
    date_modified = Column(DateTime(0), unique=True, nullable=False)
    image = Column(BLOB, nullable=True)

    def __init__(self , name:str , price:str  , amount:str,  date_add:None,date_modified:None, image=None):
        self.name = name
        self.price = price
        self.amount = amount
        self.date_add = date_add
        self.date_modified = date_modified
        self.image = image

class Purchase_record(Base):
    
    __tablename__ = 'purchase_record'

    id = Column(Integer, primary_key=True, autoincrement=True)
    buyer = Column(String(80), unique=True, nullable=False)
    purchase_time = Column(DateTime(0), nullable=False)
    product_item = Column(String(80), unique=True, nullable=False)
    item_id = Column(Integer, unique=True, nullable=False)
    product_amount = Column(Integer, unique=True, nullable=False)
    total = Column(Integer, unique=True, nullable=False)
    buyer_balance = Column(Integer, unique=True, nullable=False)
    after_purchase_balance = Column(Integer, unique=True, nullable=False)

    def __init__(self , buyer:str , purchase_time:None  , product_item:str, product_amount:int , total:int , item_id:int,buyer_balance:int,after_purchase_balance:int):
        self.buyer = buyer
        self.purchase_time = purchase_time
        self.product_item = product_item
        self.product_amount = product_amount
        self.total = total
        self.item_id = item_id
        self.buyer_balance = buyer_balance
        self.after_purchase_balance = after_purchase_balance
