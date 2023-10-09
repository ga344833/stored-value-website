<template>
    <h2 class="text-start">simulation shopping place</h2>
    <p></p>
    <div class="container">
      <div class="row row-cols-3">
        <div class="col" v-for="(product,index) in productsData" :key="product.id">
            <div class="card" style="width: 18rem;">
              <div class="card-body">
                <h5 class="card-title">{{product.name}}</h5>
                <p class="card-text">價格 : {{product.price}}</p>
                <p class="card-text">數量 : {{product.amount}}</p>
                <PurchaseForm :product="product" :account_balance="this.account_balance"></PurchaseForm>
              </div>
            </div>
          <p v-if="(index + 1) % 2 === 0"></p>
      </div>
    </div>
   </div>
  </template>
  
  <script>
  import axios from "axios";
  import PurchaseForm from "@/components/User/Product/PurchaseForm.vue";

  export default {
    name: "UserCard",
    props: {
      showCards: Boolean, // 通過 props 接收 showCards 屬性
    },
    data() {
    return {
      productsData: [],
      account_balance:0,
      token: "",
    };
  },
  components: {
    PurchaseForm,
  },
  created() { // 讀取JWT TOKEN
    this.token = localStorage.getItem("token");
    if (this.token) {
      this.fetchProductsData();
    } else {
      console.error("No valid token found.");
    }
  },
  methods: {
    fetchProductsData() {  // 1. 比對 token 2.獲取客戶資訊
      const headers = {
        Authorization: `Bearer ${this.token}`,
      };
      axios
        .get("/api/products", { headers })
        .then((response) => {
          this.productsData = response.data.allinfo;
          axios
          .get("/api/account/profile", { headers })
          .then((res) =>{
            this.account_balance = res.data.Account.balance;
            })
          })
        .catch((error) => {
          console.error("Error fetching customer data:", error);
        });
    },
  },
  };
  </script>