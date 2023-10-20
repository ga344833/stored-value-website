import { createApp } from 'vue'
import App from './App.vue'
import { createRouter,createWebHistory  } from 'vue-router'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
import '../node_modules/timeline-vuejs/dist/timeline-vuejs.css'

import LoginPage from "./pages/LoginPage.vue"

// 用戶
import UserPage from "./pages/User/UserPage.vue"
import UserhomePage from "./pages/User/UserhomePage.vue"

import InfoPage from "./pages/User/InfoPage.vue"
import BankcardPage from "./pages/User/BankcardPage.vue"
import PurchaseRecordPage from "./pages/User/PurchaseRecordPage.vue"
import TopupRecordPage from "./pages/User/TopupRecordPage.vue"

import IntroPage from "./pages/User/IntroPage.vue"



// 客服
import CustomerPage from "./pages/Customer/CustomerPage.vue"
import CustomerhomePage from "./pages/Customer/CustomerhomePage.vue"

import UserviewPage from "./pages/Customer/UserviewPage.vue"
import UserDetailPage from "./pages/Customer/UserDetailPage.vue"

import ProductviewPage from "./pages/Customer/ProductviewPage.vue"
import BankcardDetailPage from "./pages/Customer/BankcardDetailPage.vue"

import AllPurchaseRecordPage from "./pages/Customer/AllPurchaseRecordPage.vue"
import AllTopupRecordPage from "./pages/Customer/AllTopupRecordPage.vue"
import DepositDetailPage from "./pages/Customer/DepositDetailPage.vue"
import RecordPage from "./pages/Customer/RecordPage.vue"



const routes =[
    {
        path: '/',
        name: "LoginPage",
        component : LoginPage
    },
    {
        path:'/user',
        name: "UserPage",
        component : UserPage,
        children:[
            {
                path:'homepage',
                name: "UserhomePage",
                component : UserhomePage,
            },
            {
                path:'intro',
                name: "IntroPage",
                component : IntroPage,
            },
            {
                path:'info',
                name: "InfoPage",
                component : InfoPage,
            },
            {
                path:'bankcard',
                name: "BankcardPage",
                component : BankcardPage,
            },
            {
                path:'purchaserecord',
                name: "PurchaseRecordPage",
                component : PurchaseRecordPage,
            },
            {
                path:'topuprecord',
                name: "TopupRecordPage",
                component : TopupRecordPage,
            }
        ]
    },

    {
        path:'/customer',
        name: "CustomerPage",
        component : CustomerPage,
        children:[
            {
                path:'homepage',
                name: "CustomerhomePage",
                component : CustomerhomePage,
            },
            {
                path:'allpurchaserecord',
                name: "AllPurchaseRecordPage",
                component : AllPurchaseRecordPage,
            },
            {
                path:'deposit/:customerId',
                name: "DepositDetailPage",
                component : DepositDetailPage,
            },
            {
                path:'users',
                name: "UserviewPage",
                component : UserviewPage,
            },
            {
                path:'users/:customerId',
                name: "UserDetailPage",
                component : UserDetailPage,
            },
            {
                path:'products',
                name: "ProductviewPage",
                component : ProductviewPage,
            },
            {
                path:'bankcards/:bankcardId',
                name: "BankcardDetailPage",
                component : BankcardDetailPage,
            },
            {
                path:'record',
                name: "RecordPage",
                component : RecordPage,
            },
            {
                path:'topuprecord',
                name: "AllTopupRecordPage",
                component : AllTopupRecordPage,
            }
        ]
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes: routes,
  })

createApp(App)
.use(router)
.mount('#app')
