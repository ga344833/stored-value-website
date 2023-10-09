<template>
    <div class="container" v-if="showCards">
        <div class="row">
    <div class="col">
        <div class="card">
    <div class="card-header">
    當前用戶總數 :
    </div>
    <div class="card-body" id="mySpecialCard" v-if="showCards">
    <h5 class="card-title">{{CustomersSum}}</h5>
    <router-link to="/customer/users" class="btn btn-primary">客戶列表</router-link>
        </div>
    </div>
    </div>
    <div class="col">
        <div class="card">
    <div class="card-header">
    客戶資料待審核筆數 : 
    </div>
    <div class="card-body">
    <h5 class="card-title">{{CustomersWaitingSum}}</h5>
    <router-link to="/customer/users" class="btn btn-primary">客戶審核列表</router-link>
        </div>
    </div>
    </div>
    <div class="col">
        <div class="card">
    <div class="card-header">
    當前商品種類 : 
    </div>
    <div class="card-body">
    <h5 class="card-title">{{ProductSum}}</h5>
    <router-link to="/customer/products" class="btn btn-primary">商品列表</router-link>
        </div>
    </div>
    </div>
  </div>
    </div>
    <p></p>
    <div class="card">
    <div class="card-header">
    入金待審核筆數 : 
    </div>
    <div class="card-body">
    <h5 class="card-title">XXXYYY</h5>
    <a href="#" class="btn btn-primary">入金審查列表</a>
        </div>
    </div>
    <p></p>
  </template>
  
  <script>
  import axios from "axios";
  export default {
    name: "CustomerCard",
    props: {
      showCards: Boolean, // 通過 props 接收 showCards 屬性
    },
    data() {
    return {
      CustomersSum: "",
      ProductSum: "",
      CustomersWaitingSum: "",
      token: "",
    };
  },
  created() { // 讀取JWT TOKEN
    this.token = localStorage.getItem("token");
    if (this.token) {
      this.fetchData();
    } else {
      console.error("No valid token found.");
    }
  },
  methods: {
    fetchData() {  // 1. 比對 token 2.獲取客戶資訊
      const headers = {
        Authorization: `Bearer ${this.token}`,
      };
      axios
        .get("/api/customers", { headers })
        .then((response) => {
          this.CustomersSum = response.data.allsum;
          this.CustomersWaitingSum = response.data.waitingsum;
          axios
          .get("/api/products", { headers })
          .then((response) => {
            this.ProductSum = response.data.allsum;
          })
        })
        .catch((error) => {
          console.error("Error fetching customer data:", error);
        });
    },
  },
  };
  </script>