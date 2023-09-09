from flask import Flask
from router import allRoute
from sqlalchemy import create_engine , inspect
import configparser
from OrmModels.Base import Base

config = configparser.ConfigParser()
config.read('config.ini')

app = Flask(__name__)
app.register_blueprint(allRoute, url_prefix="/api")

# create table & migrate
print("=")

if __name__ == '__main__':
    app.run(host= '0.0.0.0' , port='3000')
