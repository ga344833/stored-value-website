<template>
    <div class="CreateUserAccount"></div>
    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#AccountModal" @click="beforecreate">
  開通帳戶
</button>

<!-- Modal -->
<div class="modal fade" id="AccountModal" tabindex="-1" aria-labelledby="AccountModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="AccountModalLabel">開通虛擬帳戶</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <form class="row g-3 needs-validation" novalidate>
  <div class="col-md-6">
    <label for="account_number" class="form-label">帳戶號碼</label>
    <input type="text" class="form-control" id="phone" v-model="account_number" required>
    <div class="valid-feedback">
    </div>
  </div>
  <div class="col-md-6">
    <label for="balance" class="form-label">餘額</label>
    <input type="text" class="form-control" id="phone" v-model="balance" required>
    <div class="valid-feedback">
    </div>
  </div>
</form>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">關閉</button>
        <button type="button" class="btn btn-primary" data-bs-dismiss="modal" @click="createuseraccount">確定</button>
      </div>
    </div>
  </div>
</div>
</template>
<script>
import axios from "axios";
export default {
  name: "CreateUserAccount", 
  data(){
    return{
      token: "",
      account_number:"",
      balance:"",
      accountinfo:"",
    }
  },
  created() {
    this.accountinfo = localStorage.getItem("accountinfo");
    this.info_state = localStorage.getItem("info_state");
    this.token = localStorage.getItem("token");
  },
  methods:{
    beforecreate(){
      this.accountinfo = localStorage.getItem("accountinfo");
      this.info_state = localStorage.getItem("info_state");
      if (this.accountinfo != "未開通"){
        alert("該用戶已開通帳戶");
        window.location.reload();
        return;
      }
      if (this.info_state != "approved"){
        alert("該用戶尚未通過身分驗證");
        window.location.reload();
        return;
      }
    },
    createuseraccount(){
      const headers = {
        Authorization: `Bearer ${this.token}`,
      };
      const customerId = this.$route.params.customerId;
      const AccountData = {
        account_number: this.account_number,
        balance: this.balance,
      };
      
      axios
      .post(`/api/account/${customerId}`,AccountData,{ headers })
      .then((res) => {
        alert(res.data.message);
        window.location.reload(); 
      })
      .catch((error) => {
          console.error(error);
          alert("Register Fail,Please check python");
          window.location.reload();
        });
    }
  }
};
</script>