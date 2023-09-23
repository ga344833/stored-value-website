import { createApp } from 'vue'
import App from './App.vue'
import { createRouter,createWebHistory  } from 'vue-router'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
import '../node_modules/timeline-vuejs/dist/timeline-vuejs.css'

import LoginPage from "./pages/LoginPage.vue"

import UserPage from "./pages/UserPage.vue"
import InfoPage from "./pages/InfoPage.vue"
import IntroPage from "./pages/IntroPage.vue"

import CustomerPage from "./pages/CustomerPage.vue"
import CashPage from "./pages/CashPage.vue"
import RecordPage from "./pages/RecordPage.vue"

const routes =[
    {
        path: '/',
        component : LoginPage
    },
    {
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
        ]
    },
    {
        path:'/customer',
        component : CustomerPage,
        children:[
            {
                path:'cash',
                component : CashPage,
            },
            {
                path:'record',
                component : RecordPage,
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
