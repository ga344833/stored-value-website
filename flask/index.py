from flask import Flask
from router import allRoute
from sqlalchemy import create_engine , inspect
import configparser
from OrmModels.Base import Base

config = configparser.ConfigParser()
config.read('config.ini')

# 初始化 Redis 连接
redis_host = config['REDIS']['host']
redis_port = int(config['REDIS']['port'])
redis_password = config['REDIS']['password']

app = Flask(__name__)
app.secret_key = config['INDEX']['SECRET_KEY']
app.register_blueprint(allRoute, url_prefix="/api")

# create table & migrate
print("=")

if __name__ == '__main__':
    app.run(port='5000')
