<template>
    <div class="VerifyUserInfo"></div>
    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal" @click="beforecreate">
  審核客戶資訊
</button>

<!-- Modal -->
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">審核客戶資訊</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <form class="row g-3 needs-validation" novalidate>
  <div class="col-md-9">
    <label for="pw" class="form-label">客服密碼</label>
    <input type="tel" class="form-control" id="phone" v-model="pw" required>
    <div class="valid-feedback">
    </div>
  </div>
  <div class="col-md-3">
    <label for="validationCustom04" class="form-label">State</label>
    <select class="form-select" id="validationCustom04" v-model="state" required>
      <option selected disabled value="">State</option>
      <option>approved</option>
      <option>rejected</option>
    </select>
    <div class="invalid-feedback">
      Please select a valid state.
    </div>
  </div>
</form>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">關閉</button>
        <button type="button" class="btn btn-primary" data-bs-dismiss="modal" @click="verifyuserinfo">確定</button>
      </div>
    </div>
  </div>
</div>
</template>
<script>
import axios from "axios";
export default {
  name: "VerifyUserInfo", 
  data(){
    return{
      token: "",
      state:"",
    }
  },
  created() {
    this.token = localStorage.getItem("token");
  },
  methods:{
    beforecreate(){
      this.info_idnum = localStorage.getItem("info_idnum");
      if (this.info_idnum === "null"){
        alert("用戶未填寫身分證");
        window.location.reload();
        return;
      }
    },
    verifyuserinfo(){
      const headers = {
        Authorization: `Bearer ${this.token}`,
      };
      const customerId = this.$route.params.customerId;
      const State = {
        state: this.state
      };
      console.log(customerId);
      console.log(headers);
      axios
      .patch(`/api/customer/${customerId}/verify`,State,{ headers })
      .then((res) => {
        alert(res.data.message);
        window.location.reload(); 
      })
      .catch((error) => {
          console.error(error);
          alert("Register Fail,Please check python");
        });
    }
  }
};
</script>