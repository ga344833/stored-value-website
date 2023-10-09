# 模擬儲值及客服管理網站網站實作

以Mysql為資料庫、flask為後端、Vue為前端所構建的簡易模擬儲值及客服管理網站

![image](https://github.com/ga344833/Simulation-payment-system/assets/32910355/465ef740-13f9-46b9-8ddc-72ae22f632d3)


包含以下功能 :

* 登入系統 :
  
1.分為客服、會員兩種身分，以 JWT TOKEN 識別登入身分並各自擁有其操作介面
  
2.註冊及忘記密碼

* 客服介面 : 客服可透過各列表查看各項紀錄、並擁有審核客戶資料、開通客戶虛擬帳戶、修改與新增商品列表等權限功能
  
1.包含客戶列表、商品列表、儲值紀錄、購買紀錄

* 會員介面 : 會員透過註冊後可登入系統、於個人介面完善資料提交審核，操作客服所開通的帳戶、進行儲值與購物

1. 包含購物介面、個人資料、儲值紀錄、購買紀錄
