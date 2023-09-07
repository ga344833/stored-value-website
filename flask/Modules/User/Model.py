from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
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

class User(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    fullname = Column(String(80), unique=True, nullable=False)
    phone = Column(String(80), unique=True, nullable=False)
    email = Column(String(80), unique=True, nullable=False)
    username = Column(String(80), unique=True, nullable=False)
    password = Column(String(80), unique=True, nullable=False)
    gender = Column(String(1), unique=True, nullable=False)
    internal = Column(String(1), unique=True, nullable=False)

    def __init__(self , fullname:str , phone:str , email:str , username:str, password:str , gender:str , internal:str):
        self.fullname = fullname
        self.phone = phone
        self.email = email
        self.username = username
        self.password = password
        self.gender = gender
        self.internal = internal
    
    def serialize(self):
        user_schema = UserSchema()
        return user_schema.dump(self)