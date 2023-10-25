# 用戶儲值與客服管理

整合Vue Bootstrap、Flask MVC、MySQL 開發
---
### Flask MVC 分層架構
#### Router <=> Controller <=> Service <=> Repository <=> Model <=> DB

![image](https://github.com/ga344833/stored-value-website/assets/32910355/be2e8dbe-5e86-4719-97c2-4e11ba6fbe18)

* dtos : (Data Transfer Objects) 定義數據傳輸的格式
	* 可幫助數據從client端傳送到server端或其他模塊
	  
* Model : 模型層、用於定義Database
	* 通常使用ORM來定義DB
	  
* UserController : 控制器層、處理HTTP請求、調用適當的服務
	* function ，各項功能(登入、創建用戶等)都寫在這裡
	  
* UserRepo : 儲存庫層、執行DataBase查詢和操作
	* 和DB互動並處理儲存、檢索數據等細節
	  
* UserService : 服務層、包含應用程式的核心邏輯、處裡來自Controller的請求
	* 與各個模塊互動最頻繁的位置
	* 初始化連結儲存層、function 連結dtos獲取資訊甚至檢核
	* 檢核完畢後再次呼叫儲存層操作DB
	* 動作完成後將結果回傳至Controller
--- 
### Vue 
使用 router-view 作為 變動組件，層層包裹
如同以下模板 ，採取主程式 > 頁面 > 組件等方式分層進行管理編程

```	App (主程式) :
		Login (頁面)
		User (頁面)
			UserNavBar (組件)
		Customer (頁面)
			CusNavBar (組件)
		Info (頁面)
		intro (頁面)
		.... ```

####  App.Vue
  作為整支Vue最底部的組件，編輯頁面上層與底層，使用router-view將網頁中間區塊，以不同的分頁作為顯示對象，例如Login、User等等
```
<template>
  <div id="app">
    <div class="text-center my-3">
      <div class="header-container">
        <h2>johney simulation pay system</h2>
      </div>
      <div class="container">
            <router-view></router-view> <!-- 中間的組件 隨著router 變動 -->
      </div>
    </div>
    <div class="fixed-bottom">
      <footer class="bg-light text-center text-lg-center">
        <div class="footer-container">
          © 2023 Copyright: francischi.com
        </div>
      </footer>
    </div>
  </div>
</template>
```
#### main.js
將程式的routes path定義，以便於不同的畫面呈現，此時App依然作為底層模板
```
const routes =[
    {
        path: '/',
        component : LoginPage
    }]
```
#### Pages
頁面存放處，其中 main.js 可設置 children 將組件共用
```
path:'/user',
        component : UserPage,
        children:[
            {
                path:'intro',
                component : IntroPage,
            },
            {
                path:'info',
                component : InfoPage,
            }
```

