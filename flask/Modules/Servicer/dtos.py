from  abc import abstractmethod

class dto:
    @abstractmethod
    def check():
        return 

# class loginDto():
#     def __init__(self , userName:str , passWord:str):
#         self.userName = userName
#         self.passWord = passWord
    
#     def check(self):
#         if self.userName == "":
#             raise ValueError('user_name required')
#         if self.passWord == "":
#             raise ValueError('pass_word required')

# class registerDto():
#     def __init__(self , fullname:str , phone:str , email:str , username:str , password:str , gender:str):
#         self.fullname = fullname
#         self.phone = phone
#         self.email = email
#         self.username = username
#         self.password = password
#         self.gender = gender
    
#     def check(self):
#         # 簡易檢查:
#         if "@" not in self.email:
#             raise ValueError('email Format does not match')
            
#         if 10 != len(self.phone):
#             raise ValueError('phone Format does not match')
            
#         if 8 > len(self.username):
#             raise ValueError('username length does not match')
            
#         if 8 > len(self.password):
#             raise ValueError('password length does not match')
            
#         if self.fullname == None:
#             raise ValueError('need fullname')

#         if self.gender == None:
#             raise ValueError('need gender')


