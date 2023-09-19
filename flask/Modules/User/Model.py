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

    def __init__(self , fullname:str , phone:str , email:str , username:str, password:str , gender:str , internal:str , register_time:None
                 ,country=None, idtype=None, idnumber=None, profile_image=None):
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
    
    def serialize(self):
        user_schema = UserSchema()
        return user_schema.dump(self)