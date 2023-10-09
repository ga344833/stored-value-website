from .UserService import UserService 
from ..payment.PaymentService import PaymentService
from  .dtos import loginDto,registerDto,perfectInfoDto,ImageDto,VerifyCustomerDto,CreateBankcardDto,VerifyBankcardDto,CreateAccountDto,CreateProductDto,DeleteProductDto,PatchProductDto,CreatePurchaseRecordDto,ProcessPurchaseDto
from flask import request,make_response,jsonify,g,Response,render_template
class UserController:
    def __init__(self):
        self.UserService = UserService()
        self.PaymentService = PaymentService()

    def login(self):
        print('--UserController stage--')
        try:
            if request.is_json:
                params = request.get_json()
                userName = params.get('username', None)
                passWord = params.get('password', None)
                print('username : '+str(userName))
                print('passWord : '+str(passWord))
                dto = loginDto(userName , passWord)
            else:
                raise ValueError('data type error')    

            result = self.UserService.login(dto)
            
            token = self.UserService.generate_token(result[0])
            return make_response(
                jsonify(
                    {
                        "success":True,
                        "code":result[1],
                        "token":token,
                    }
                )
            )
        except Exception as msg:
            print(msg)
            return make_response(
                jsonify(
                    {
                        "success":False,
                        "message":"no user info"
                    }
                ),
                400
            )

    def create(self):
        print('--UserController stage--')
        try:
            if request.is_json:
                data = request.get_json()
                fullname = data.get("name")
                phone = data.get("phone")
                email = data.get("email")
                username = data.get("username")
                password = data.get("password")
                gender = data.get("gender")
                print('name: '+str(fullname))
                print('pw: '+str(password))
                print("--1--")
                dto = registerDto(fullname , phone , email , username , password , gender)
            else:
                raise ValueError('data type error')    

            result = self.UserService.create(dto)
            print("--3--")
            return make_response(
                jsonify(result),
            )
        except Exception as msg:
            return make_response(
                jsonify(
                    {
                        "success":False,
                        "message":str(msg)
                    }
                ),
                400
            )

    def getCustomersInfo(self):
        print('--UserController stage--')
        result = self.UserService.getCustomersInfo()
        return make_response(jsonify({'success':True,'allinfo':result[0],'waitinginfo':result[1],'allsum':len(result[0]),'waitingsum':len(result[1])}))
        
    def getBankcardsInfo(self):
        print('--UserController stage--')
        result = self.UserService.getBankcardsInfo()
        return make_response(jsonify({'success':True,'allinfo':result[0],'waitinginfo':result[1],'allsum':len(result[0]),'waitingsum':len(result[1])}))

    def getproductsInfo(self):
        print('--UserController stage--')
        result = self.UserService.getproductsInfo()
        return make_response(jsonify({'success':True,'allinfo':result,'allsum':len(result)}))



    def getCustomerInfo(self,customer_id):
        print('--UserController stage--')
        servicer_id = g.token.get('sub')
        print("servicer_id : "+str(servicer_id))
        if servicer_id == 1: ## 篩選是否為客服人員、避免API被盜用、後續再規劃
            result = self.UserService.getCustomerById(customer_id)
            return result 
        else:
            return make_response(jsonify({'success':False,'message':'Non service staff'}))

    def verifyCustomer(self,customer_id):
        print('--UserController stage--')
        servicer_id = g.token.get('sub')
        print("servicer_id : "+str(servicer_id))
        data = request.get_json()
        state = data.get("state")
        dto = VerifyCustomerDto(customer_id,state)
        if servicer_id == 1: ## 篩選是否為客服人員、避免API被盜用、後續再規劃
            result = self.UserService.verifyCustomer(dto)
            return make_response(jsonify({'success':True,'message':'state success changed'})) 
        else:
            return make_response(jsonify({'success':False,'message':'Non service staff'}))

    def get_customer_profile(self):      
        print('--UserController stage--')
        try:
            # 从 JWT token 中获取客户的用户 ID
            customer_id = g.token.get('sub')
            print("customer_id : "+str(customer_id))
            # 使用 customer_id 查询客户的个人信息
            customer_info = self.UserService.getCustomerById(customer_id)
            # print(customer_info)
            if customer_info:
                return make_response(
                jsonify(
                    {   "success": True,
                        "name":customer_info['fullname'],
                        "state": customer_info['state'],
                        "phone":customer_info['phone'],
                        "email":customer_info['email'],
                        "country":customer_info['country'],
                        "idtype":customer_info['idtype'],
                        "idnumber":customer_info['idnumber'],
                        "forzen":customer_info['forzen'],
                        "gender":customer_info['gender'],
                        "register_time":customer_info['register_time'],
                        "image":customer_info['profile_image'],
                        "username":customer_info['username'],
                        "password":customer_info['password']
                    }
                ),
            )
            else:
                return make_response(jsonify({'success':False,'message':"Customer not found"}),404)
        except Exception as e:
            return make_response(jsonify({'success':False,'message':str(e)}))

    def get_bankcard_profile(self):      
        print('--UserController stage--')
        try:
            # 从 JWT token 中获取客户的用户 ID
            customer_id = g.token.get('sub')
            print("customer_id : "+str(customer_id))
            # 使用 customer_id 查询客户的个人信息
            BankcardInfo = self.UserService.getBankcardById(customer_id)
            # print(customer_info)
            if BankcardInfo:
                return make_response(
                jsonify(
                    {   "success": True,
                        "bankcard": BankcardInfo,
                        "state": BankcardInfo['state']
                    }
                ),
            )
            
            else:
                return make_response(jsonify({'success':False,'message':"Bankcard not found"}),404)
        except Exception as e:
            return make_response(jsonify({'success':False,'message':str(e)}))

    def patch_customer_profile(self):      
        try:
            # 从 JWT token 中获取客户的用户 ID
            customer_id = g.token.get('sub')
            print("customer_id : "+str(customer_id))
            # 使用 customer_id 查询客户的个人信息
            if request.is_json:
                data = request.get_json()
                country = data.get("country")
                idtype = data.get("idtype")
                idnumber = data.get("idnumber")
                dto = perfectInfoDto(customer_id,country , idtype , idnumber)
                print(dto.customer_id)
            patch_customer_info = self.UserService.patchCustomerInfo(dto)
            if patch_customer_info:
                return make_response(
                jsonify(
                    {   "success": patch_customer_info['success'],
                        "message": patch_customer_info['message']
                    }
                ),
            )
            else:
                return make_response(jsonify({'success':False,'message':"Customer not found"}),404)
        except Exception as e:
            return make_response(jsonify({'success':False,'message':str(e)}),500)

    def patch_product_profile(self):      
        try:
            # 从 JWT token 中获取客户的用户 ID
            servicer_id = g.token.get('sub')
            print("customer_id : "+str(servicer_id))
            if servicer_id == 1:
            # 使用 customer_id 查询客户的个人信息
                if request.is_json:
                    data = request.get_json()
                    product_id = data.get("id")
                    name = data.get("name")
                    price = data.get("price")
                    amount = data.get("amount")
                    dto = PatchProductDto(product_id,name,price,amount)
                patch_product_info = self.UserService.patchProductInfo(dto)
                if patch_product_info:
                    return make_response(
                    jsonify(
                        {   "success": patch_product_info['success'],
                            "message": patch_product_info['message']
                        }
                    ),
                )
                else:
                    return make_response(jsonify({'success':False,'message':"Customer not found"}),404)
            else:
                return make_response(jsonify({'success':False,'message':'Non service staff'}),400)
        except Exception as e:
            return make_response(jsonify({'success':False,'message':str(e)}),500)

    def upload_image(self):
        print('--UserController stage--')
        try:
            # 从 JWT token 中获取客户的用户 ID
            customer_id = g.token.get('sub')
            print("customer_id : "+str(customer_id))
            # 使用 customer_id 查询客户的个人信息
            if 'file' not in request.files:
                return make_response(jsonify({'success': False, 'message': 'No file part'}), 400)
            file = request.files['file']
            # 检查文件名是否为空
            if file.filename == '':
                return make_response(jsonify({'success': False, 'message': 'No selected file'}), 400)
            dto = ImageDto(customer_id,file)
            upload_info = self.UserService.uploadInfo(dto)
            #patch_customer_info = self.UserService.patchCustomerInfo(dto)
            if upload_info:
                return make_response(
                jsonify(
                    {   "success": upload_info['success'],
                        "message": upload_info['message']
                    }
                ),
            )
            else:
                return make_response(jsonify({'success':False,'message':"Customer not found"}),404)
        except Exception as e:
            return make_response(jsonify({'success':False,'message':str(e)}),500)
        
    def createbankcard(self):
        print('--UserController stage--')
        try:
            customer_id = g.token.get('sub')
            print("customer_id : "+str(customer_id))
            if request.is_json:
                data = request.get_json()
                card_number = data.get("card_number")
                bank = data.get("bank")
                dto = CreateBankcardDto(customer_id,card_number,bank)
            else:
                raise ValueError('data type error')    

            result = self.UserService.createbankcard(dto)
            
            return make_response(
                jsonify(result))
        except Exception as msg:
            return make_response(
                jsonify(
                    {
                        "success":False,
                        "message":str(msg)
                    }
                ),
                400
            )

    def upload_bankcard_image(self):
        print('--UserController stage--')
        try:
            # 从 JWT token 中获取客户的用户 ID
            customer_id = g.token.get('sub')
            print("customer_id : "+str(customer_id))
            # 使用 customer_id 查询客户的个人信息
            if 'file' not in request.files:
                return make_response(jsonify({'success': False, 'message': 'No file part'}), 400)
            file = request.files['file']
            # 检查文件名是否为空
            if file.filename == '':
                return make_response(jsonify({'success': False, 'message': 'No selected file'}), 400)
            dto = ImageDto(customer_id,file)
            upload_info = self.UserService.uploadBankcardInfo(dto)
            if upload_info:
                return make_response(
                jsonify(
                    {   "success": upload_info['success'],
                        "message": upload_info['message']
                    }
                ),
            )
            else:
                return make_response(jsonify({'success':False,'message':"Customer not found"}),404)
        except Exception as e:
            return make_response(jsonify({'success':False,'message':str(e)}),500)
 
    def getBankcardInfo(self,customer_id):
        print('--UserController stage--')
        servicer_id = g.token.get('sub')
        print("servicer_id : "+str(servicer_id))
        if servicer_id == 1: ## 篩選是否為客服人員、避免API被盜用、後續再規劃
            result = self.UserService.getBankcardById(customer_id)
            return result 
        else:
            return make_response(jsonify({'success':False,'message':'Non service staff'}))

    def verifyBankcard(self,customer_id):
        print('--UserController stage--')
        servicer_id = g.token.get('sub')
        print("servicer_id : "+str(servicer_id))
        data = request.get_json()
        state = data.get("state")
        dto = VerifyBankcardDto(customer_id,state)
        if servicer_id == 1: ## 篩選是否為客服人員、避免API被盜用、後續再規劃
            result = self.UserService.verifyBankcard(dto)
            return make_response(jsonify({'success':True,'message':'state success changed'})) 
        else:
            return make_response(jsonify({'success':False,'message':'Non service staff'}))

    def CreateAccount(self,customer_id):
        try:
            servicer_id = g.token.get('sub')
            print("servicer_id : "+str(servicer_id))
            if servicer_id == 1: ## 篩選是否為客服人員、避免API被盜用、後續再規劃
                if request.is_json:
                    data = request.get_json()
                    account_number = data.get("account_number")
                    balance = data.get("balance")
                    dto = CreateAccountDto(customer_id,balance,account_number)
                account_info = self.UserService.CreateAccount(dto)
                if account_info:
                    return make_response(jsonify(account_info))
                else:
                    return make_response(jsonify({'success':False,'message':"Customer not found"}),404)
        except Exception as e:
            return make_response(jsonify({'success':False,'message':str(e)}),500)

    def get_account_profile(self):      
        print('--UserController stage--')
        try:
            customer_id = g.token.get('sub')
            print("customer_id : "+str(customer_id))
            AccountInfo = self.UserService.getAccountById(customer_id)
            if AccountInfo:
                return make_response(jsonify({"success": True,
                        "Account": AccountInfo}),)
            else:
                return make_response(jsonify({'success':False,'message':"Account not found"}),404)
        except Exception as e:
            return make_response(jsonify({'success':False,'message':str(e)}))

    def getAccountInfo(self,customer_id):
        print('--UserController stage--')
        servicer_id = g.token.get('sub')
        print("servicer_id : "+str(servicer_id))
        if servicer_id == 1: ## 篩選是否為客服人員、避免API被盜用、後續再規劃
            print("customer_id : "+str(customer_id))
            result = self.UserService.getAccountById(customer_id)
            return result 
        else:
            return make_response(jsonify({'success':False,'message':'Non service staff'}))
 
    def Accountdeposit(self):
        customer_id = g.token.get('sub')
        data = request.get_json()
        amount = data.get("amount")
        Account_info = self.UserService.getAccountById(customer_id)
        account_id = Account_info['account_number']
        result = self.PaymentService.Accountdeposit(customer_id,amount,account_id)
        result = render_template('payment.html', form_html=result)
        return make_response(jsonify({'success':True,'message':result}))
    
    def Receiveresult(self):
        print(request.form)
        amount = int(request.form['amount'])
        customer_id = int(request.form['CustomField1'])
        account_id = request.form['CustomField2']
        remark = request.form['CustomField3']
        if 'testpay' == request.form['CustomField4']:
            # step 1 把錢存到 customer_balance_deposit，帶上account_id、remark
            # state = waiting
            dto = CreateAccountDto(customer_id,account_id,amount,remark)
            result = self.UserService.CreateBalanceDeposit(dto)
            return '1|OK'
        
    def createproduct(self):
        print('--UserController stage--')
        try:
            servicer_id = g.token.get('sub')
            print("customer_id : "+str(servicer_id))
            if servicer_id == 1:
                if request.is_json:
                    data = request.get_json()
                    name = data.get("name")
                    price = data.get("price")
                    amount = data.get("amount")                    
                    dto = CreateProductDto(name,price,amount)
                else:
                    raise ValueError('data type error')    

                result = self.UserService.createproduct(dto)
            
                return make_response(
                    jsonify(result))
            else:
                return make_response(jsonify({'success':False,'message':'Non service staff'}),400)
        except Exception as msg:
            return make_response(jsonify({
                        "success":False,
                        "message":str(msg)
                    }),400)
        
    def deleteproduct(self):
        print('--UserController stage--')
        try:
            servicer_id = g.token.get('sub')
            print("customer_id : "+str(servicer_id))
            if servicer_id == 1:
                if request.is_json:
                    data = request.get_json()
                    name = data.get("name")                   
                    dto = DeleteProductDto(name)
                else:
                    raise ValueError('data type error')    

                result = self.UserService.deleteproduct(dto)
            
                return make_response(
                    jsonify(result))
            else:
                return make_response(jsonify({'success':False,'message':'Non service staff'}),400)
        except Exception as msg:
            return make_response(jsonify({
                        "success":False,
                        "message":str(msg)
                    }),400)

    def CreatePurchaseRecord(self):
        try:
            customer_id = g.token.get('sub')
            if request.is_json:
                data = request.get_json()
                buyer = data.get("buyer")
                product_item = data.get("product_item")
                item_id = data.get("item_id")
                product_amount = data.get("product_amount")
                total = data.get("total")
                buyer_balance = data.get("buyer_balance")
                after_purchase_balance = data.get("after_purchase_balance")
                dto = CreatePurchaseRecordDto(customer_id,buyer,product_item,item_id,product_amount,total,buyer_balance,after_purchase_balance)
            info = self.UserService.CreatePurchaseRecord(dto)
            if info:
                return make_response(jsonify(info))
            else:
                return make_response(jsonify({'success':False,'message':"Customer not found"}),404)
        except Exception as e:
            return make_response(jsonify({'success':False,'message':str(e)}),500)
        
    def ProcessPurchase(self):
        try:
            customer_id = g.token.get('sub')
            if request.is_json:
                data = request.get_json()
                product_item = data.get("product_item")
                product_amount = data.get("product_amount")
                total = data.get("total")
                dto = ProcessPurchaseDto(customer_id,product_item,product_amount,total)
            info = self.UserService.ProcessPurchase(dto)
            if info:
                return make_response(jsonify(info))
            else:
                return make_response(jsonify({'success':False,'message':"Customer not found"}),404)
        except Exception as e:
            return make_response(jsonify({'success':False,'message':str(e)}),500)
        
    def GetPurchaseRecord(self):      
        print('--UserController stage--')
        try:
            customer_id = g.token.get('sub')
            print("customer_id : "+str(customer_id))            
            PurchaseRecords = self.UserService.getPurchaseRecordsById(customer_id)      
            return make_response(jsonify({"success": True,
                    "PurchaseRecords": PurchaseRecords}),)            
        except Exception as e:
            return make_response(jsonify({'success':False,'message':str(e)}))