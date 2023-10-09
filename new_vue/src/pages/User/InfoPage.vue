<template lang="html">
  <div class="cover"> 
      <p>InfoPage</p>
  </div>
  <div class="container">
    <div class="row">
      <div class="col-6">
        <div class="card">
          <div class="card-header text-start">
          客戶資料 
          </div>
            <div class="card-body">
              <dl class="row">
                <dt class="col-sm-4 with-border">姓名 : </dt>
                <dt class="col-sm-8 with-border">{{customer.name}}</dt>

                <dt class="col-sm-4 with-border">性別 : </dt>
                <dt class="col-sm-8 with-border">{{customer.gender}}</dt>

                <dt class="col-sm-4 with-border">國家 : </dt>
                <dt class="col-sm-8 with-border">{{customer.country}}</dt>

                <dt class="col-sm-4 with-border">手機 : </dt>
                <dt class="col-sm-8 with-border">{{customer.phone}}</dt>

                <dt class="col-sm-4 with-border">信箱 : </dt>
                <dt class="col-sm-8 with-border">{{customer.email}}</dt>

                <dt class="col-sm-4 with-border">帳號 : </dt>
                <dt class="col-sm-8 with-border">{{customer.username}}</dt>

                <dt class="col-sm-4 with-border">密碼 : </dt>
                <dt class="col-sm-8 with-border">{{customer.password}}</dt>

                <dt class="col-sm-4 with-border">驗證方式 : </dt>
                <dt class="col-sm-8 with-border">{{customer.idtype}}</dt>
                
                <dt class="col-sm-4 with-border">護照號碼 : </dt>
                <dt class="col-sm-8 with-border">{{customer.idnumber}}</dt>

                <dt class="col-sm-4 with-border">註冊時間 : </dt>
                <dt class="col-sm-8 with-border">{{customer.register_time}}</dt>

                <dt class="col-sm-4 with-border">審核狀態 : </dt>
                <dt class="col-sm-8 with-border">{{customer.state}}</dt>
              </dl>
            </div>
        </div>
      </div>
      <div class="col-6">
        <div class="card">
          <div class="card-header text-start">
          虛擬帳戶資料 
          </div>
            <div class="card-body">
              <dl class="row">
                <dt class="col-sm-4 with-border">持有人 : </dt>
                <dt class="col-sm-8 with-border">{{account.user}}</dt>

                <dt class="col-sm-4 with-border">帳戶 : </dt>
                <dt class="col-sm-8 with-border">{{account.account_number}}</dt>

                <dt class="col-sm-4 with-border">餘額 : </dt>
                <dt class="col-sm-8 with-border">{{account.balance}}</dt>

                <dt class="col-sm-4 with-border">狀態 : </dt>
                <dt class="col-sm-8 with-border">{{account.state}}</dt>
              </dl>
            </div>
        </div>
      </div>
    </div>
  </div>
  <p></p>
  <div class="container">
    <div class="row">
  <div class="col-6">
    <UploadUserInfo></UploadUserInfo>
  </div>
  <div class="col">
    <router-link to="/user/homepage" class="btn btn-primary">前往購物</router-link>
  </div>
  <div class="col">
    <TopUp></TopUp>
  </div>
</div>
</div>
</template>
<script>
import axios from "axios";
import UploadUserInfo from "@/components/User/UserInfo/UploadUserInfo.vue";
import TopUp from "@/components/User/top-up/TopUp.vue";
export default {
  name: "InfoPage",
  data() {
    return {
      customer:{},
      account:{},
      token:"",
    };
  },
  components:{
    UploadUserInfo,
    TopUp,
  },
  created() {
    this.token = localStorage.getItem("token");
    if (this.token) {
      this.fetchData();
    } else {
      console.error("No valid token found.");
    }
  },
  methods: {
    fetchData() {  
      const headers = {
        Authorization: `Bearer ${this.token}`,
      };
      axios
        .get("/api/customer/profile", { headers })
        .then((response) => {
          this.customer = response.data;
          axios
          .get("/api/account/profile", { headers })
          .then((response) => {
            this.account = response.data.Account;
            if(this.account.user === ""){
            this.account.user = "未開通";
          }
          localStorage.setItem("accountinfo",this.account.user);
          })
        })
        .catch((error) => {
          console.error("Error fetching customer data:", error);
        });
    },
  },
};
</script>
<style></style>
