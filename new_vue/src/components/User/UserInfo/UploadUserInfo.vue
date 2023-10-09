<template>
    <div class="UploadUserInfo"></div>
    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#UploadUserInfoModal" @click="beforecreate">
  完善個人資訊
</button>

<!-- Modal -->
<div class="modal fade" id="UploadUserInfoModal" tabindex="-1" aria-labelledby="UploadUserInfoModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="AccountModalLabel">完善個人資訊</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <form class="row g-3 needs-validation" novalidate>
  <div class="col-md-12">
    <label for="country" class="form-label">居住國家:</label>
    <input type="text" class="form-control" id="phone" v-model="country" required>
    <div class="valid-feedback">
    </div>
  </div>
  <div class="col-md-4">
    <label for="idtype" class="form-label">驗證方式</label>
    <select class="form-select" id="validationCustom04" v-model="idtype" required>
      <option selected disabled value="">Choose...</option>
      <option>駕照</option>
      <option>護照</option>
      <option>身分證</option>
    </select>
  </div>
  <div class="col-md-8">
    <label for="idnumber" class="form-label">護照號碼</label>
    <input type="text" class="form-control" id="phone" v-model="idnumber" required>
    <div class="valid-feedback">
    </div>
  </div>
</form>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">關閉</button>
        <button type="button" class="btn btn-primary" data-bs-dismiss="modal" @click="uploaduserinfo">確定</button>
      </div>
    </div>
  </div>
</div>
</template>
<script>
import axios from "axios";
export default {
  name: "UploadUserInfo", 
  data(){
    return{
      token: "",
    }
  },
  created() {
    this.token = localStorage.getItem("token");
  },
  methods:{
    beforecreate(){
      this.token = localStorage.getItem("token");
    },
    uploaduserinfo(){
      const headers = {
        Authorization: `Bearer ${this.token}`,
      };
      const UserData = {
        country: this.country,
        idtype: this.idtype,
        idnumber: this.idnumber,
      };      
      axios
      .patch(`/api/customer/profile`,UserData,{ headers })
      .then((res) => {
        alert(res.data.message);
        window.location.reload(); 
      })
      .catch((error) => {
          console.error(error);
          alert("Upload Fail,Please check python");
          window.location.reload();
        });
    }
  }
};
</script>