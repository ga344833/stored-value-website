<template>
    <div class="Topup"></div>
    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#TopupModal" @click="beforecreate">
  前往儲值
</button>

<!-- Modal -->
<div class="modal fade" id="TopupModal" tabindex="-1" aria-labelledby="TopupModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="AccountModalLabel">儲值</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <form class="row g-3 needs-validation" novalidate>
    <div class="col-md-6">
    <label for="topupamount" class="form-label">會員姓名 : {{account.user}}</label>
    <div class="valid-feedback">
    </div>
  </div>
    <div class="col-md-6">
    <label for="topupamount" class="form-label">儲值帳戶 : {{account.account_number}}</label>
    <div class="valid-feedback">
    </div>
  </div>
  <div class="col-md-6">
    <label for="topupamount" class="form-label">帳戶餘額 : {{account.balance}}</label>
    <div class="valid-feedback">
    </div>
  </div>
  <div class="col-md-6">
    <label for="topupamount" class="form-label">輸入儲值金額 : </label>
    <input type="text" class="form-control" id="phone" v-model="topupamount" required>
    <div class="valid-feedback">
    </div>
  </div>
</form>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">關閉</button>
        <button type="button" class="btn btn-primary" data-bs-dismiss="modal" @click="topup">前往儲值</button>
      </div>
    </div>
  </div>
</div>
</template>
<script>
import axios from "axios";
export default {
  props:{
    account: Object,
  },
  name: "TopUp", 
  data(){
    return{
      token: "",
      topupamount:"",
    }
  },
  created() {
    this.token = localStorage.getItem("token");
  },
  methods:{
    beforecreate(){
      this.token = localStorage.getItem("token");
      this.accountinfo = localStorage.getItem("accountinfo");
      if (this.accountinfo === "未開通"){
        alert("未開通帳戶，請聯繫客服");
        window.location.reload();
        return;
      }
    },
    topup(){
      const headers = {
        Authorization: `Bearer ${this.token}`,
      };
      const TopUpData = {
        amount:this.topupamount,
        customername:this.account.user,
        account:this.account.account_number,
      };
      axios
      .post(`/api/account/create_payment`,TopUpData,{ headers })
      .then((res) => {
        console.log(res);
        const newWindow = window.open();
        newWindow.document.write(res.data.message);
        newWindow.document.close();
        newWindow.focus();
      })
      .catch((error) => {
          console.error(error);
          alert("API response error");
        });
    }
  }
};
</script>