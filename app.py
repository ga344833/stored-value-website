 # 載入 flask
from flask import Flask, render_template,request,jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # 建立 Application 物件
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/crm'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False  # 禁止中文转义
db = SQLAlchemy(app)

    
class Userinfo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fullname = db.Column(db.String(80), unique=True, nullable=False)
    phone = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)
    gender = db.Column(db.String(1), unique=True, nullable=False)
    internal = db.Column(db.String(1), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

@app.route("/login", methods=["POST"])
def user_login():
    """
    用户登录
    :return:
    """
    users = Userinfo.query.all()
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    for user in users:
        if user.username == username and user.password == password:
            if user.internal == '1': ## 客服
                return jsonify({'code': 2, 'message': 'Login successful'})
            else: ## 客戶
                return jsonify({'code': 0, 'message': 'Login successful'})
    return jsonify({'code': 1, 'message': 'Login failed'})
    
@app.route("/RegisterPopup", methods=["POST"])
def user_Register():
    data = request.get_json()
    fullname = data.get("fullname")
    phone = data.get("phone")
    email = data.get("email")
    username = data.get("username")
    password = data.get("password")
    gender = data.get("gender")

    # 簡易檢查:
    if "@" not in email:
        return jsonify({'code': 0, 'message': 'email Format does not match'})
    if 10 != len(phone):
        return jsonify({'code': 1, 'message': 'phone Format does not match'})
    if 8 > len(username):
        return jsonify({'code': 2, 'message': 'username length does not match'})
    if 8 > len(password):
        return jsonify({'code': 3, 'message': 'password length does not match'})
    if fullname == None:
        return jsonify({'code': 4, 'message': 'need fullname'})
    if gender == None:
        return jsonify({'code': 5, 'message': 'need gender'})
    
    new_user = Userinfo(
        fullname=fullname,
        phone=phone,
        email=email,
        username=username,
        password=password,
        gender=gender,
        internal="0"
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'code': 6, 'message': 'Register success'})

@app.route("/ForgetpwPopup", methods=["POST"])
def forgetpw():
    users = Userinfo.query.all()
    data = request.get_json()
    username = data.get('username')
    print(username)
    for user in users:
        if user.username == username:
            return jsonify({'code':0,'message':user.password})
    return jsonify({'code': 1, 'message': 'no username'})
        
if __name__ == '__main__':
    app.run(host="0.0.0.0")
# app.run(port=85846) # 啟動網站server、可透過 port 參數指定阜號