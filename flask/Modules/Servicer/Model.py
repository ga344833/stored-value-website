from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,DateTime
from marshmallow import Schema, fields

Base = declarative_base()

class UserSchema(Schema):
    id = fields.Integer()
    fullname = fields.String()
    phone = fields.String()
    email = fields.String()
    username = fields.String()
    password = fields.String()
    gender = fields.String()
    internal = fields.String()
    register_time = fields.DateTime()

class User(Base):
    
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    fullname = Column(String(80), unique=True, nullable=False)
    phone = Column(String(80), unique=True, nullable=False)
    email = Column(String(80), unique=True, nullable=False)
    username = Column(String(80), unique=True, nullable=False)
    password = Column(String(80), unique=True, nullable=False)
    gender = Column(String(1), unique=True, nullable=False)
    internal = Column(String(1), unique=True, nullable=False)
    register_time = Column(DateTime(0), unique=True, nullable=False)

    def __init__(self , fullname:str , phone:str , email:str , username:str, password:str , gender:str , internal:str , register_time:None):
        self.fullname = fullname
        self.phone = phone
        self.email = email
        self.username = username
        self.password = password
        self.gender = gender
        self.internal = internal
        self.register_time = register_time
    
    def serialize(self):
        user_schema = UserSchema()
        return user_schema.dump(self)
    
class Bankcard(Base):
    
    __tablename__ = 'bankcard'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, unique=True, nullable=False)
    card_number = Column(String(80), unique=True, nullable=False)
    state = Column(String(80), unique=True, nullable=False)

    def __init__(self , user_id:int , card_number:str , state:str):
        self.user_id = user_id
        self.card_number = card_number
        self.state = state
