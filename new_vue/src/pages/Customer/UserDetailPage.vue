<template lang="html">
    <div class="cover"> 
        <p>UserDetailPage</p>
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
                  <dt class="col-sm-8 with-border">{{customer.fullname}}</dt>

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

                  <dt class="col-sm-4 with-border">身分證 : </dt>
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
      <VerifyUserInfo></VerifyUserInfo>
    </div>
    <div class="col">
      <CreateUserAccount></CreateUserAccount>
    </div>
    <div class="col">
      <VerifyUserInfo></VerifyUserInfo>
    </div>
  </div>
</div>
</template>
<script>
import axios from "axios";
import VerifyUserInfo from "@/components/Customer/UserInfo/VerifyUserInfo.vue";
import CreateUserAccount from "@/components/Customer/Account/CreateUserAccount.vue";
export default {
  name: "UserDetailPage",
  data(){
    return {
      customer:{},
      account:{},
      token:"",
    };
  },
  components:{
    VerifyUserInfo,
    CreateUserAccount,
  },
  created() {
    this.token = localStorage.getItem("token");
    if (this.token) {
      const customerId = this.$route.params.customerId;
      this.fetchData(customerId);
    } else {
      console.error("No valid token found.");
    }
  },
  methods: {
    fetchData(customerId) {
      const headers = {
        Authorization: `Bearer ${this.token}`,
      };
      axios
        .get(`/api/customer/${customerId}`, { headers })
        .then((response) => {
          this.customer = response.data;
          if(this.customer.gender === "m"){
            this.customer.gender = "男";
          }
          if(this.customer.gender === "f"){
            this.customer.gender = "女";
          }    
          localStorage.setItem("info_state",this.customer.state); 
          localStorage.setItem("info_idnum",this.customer.idnumber);        
          axios
          .get(`/api/account/${customerId}`, { headers })
          .then((response) => {
          this.account = response.data;
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
<style>
.with-border {
  border-bottom: 1px solid #ccc; /* 添加底边框样式 */
}
</style>
