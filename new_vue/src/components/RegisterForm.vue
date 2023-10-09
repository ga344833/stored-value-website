<template>
    <div class="RegisterForm"></div>
    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
  註冊
</button>

<!-- Modal -->
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">註冊</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <form class="row g-3 needs-validation" novalidate>
  <div class="col-md-6">
    <label for="name" class="form-label" >Name</label>
    <input type="text" class="form-control" id="name" v-model="name" required>
    <div class="valid-feedback">
      Please insert your name.
    </div>
  </div>
  <div class="col-md-6">
    <label for="phone" class="form-label">Phone</label>
    <input type="tel" class="form-control" id="phone" v-model="phone" required  pattern="^\d{10}$" :title="validatePhone() ? 'Valid phone' : 'Phone must be 10 digits'">
    <div class="valid-feedback">
      Please insert phone.
    </div>
  </div>
  <div class="col-md-6">
    <label for="username" class="form-label">Username</label>
    <div class="input-group has-validation">
      <input type="text" class="form-control" id="username" aria-describedby="inputGroupPrepend" v-model="username" required>
      <div class="invalid-feedback">
        Please insert username.
      </div>
    </div>
  </div>
  <div class="col-md-6">
    <label for="password" class="form-label">Password</label>
    <input type="password" class="form-control" id="password" placeholder="Password" v-model="password" required>
    <div class="invalid-feedback">
      Please insert password.
    </div>
  </div>
  <div class="col-md-3">
    <label for="gender" class="form-label">Gender</label>
    <select class="form-select" id="gender" v-model="gender" required>
      <option selected disabled value="">Gender</option>
      <option value="male">Male</option>
      <option value="female">Female</option>
    </select>
    <div class="invalid-feedback">
      Please select a valid state.
    </div>
  </div>
  <div class="col-md-9">
    <label for="email" class="form-label">Email</label>
    <input type="email" class="form-control" id="email" aria-describedby="inputGroupPrepend" v-model="email" required>
      <div class="invalid-feedback">
        Please insert Email.
      </div>
  </div>
  <div class="col-12">
    <div class="form-check">
      <input class="form-check-input" type="checkbox" value="" id="invalidCheck" required>
      <label class="form-check-label" for="invalidCheck">
        Agree to terms and conditions
      </label>
      <div class="invalid-feedback">
        You must agree before submitting.
      </div>
    </div>
  </div>
  <div class="col-12">
  </div>
</form>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">關閉</button>
        <button type="button" class="btn btn-primary" data-bs-dismiss="modal" @click="register">註冊</button>
      </div>
    </div>
  </div>
</div>
</template>
<script>
import axios from "axios";
export default {
  name: "RegisterForm", 
  data(){
    return{
      name:"",
      phone:"",
      username:"",
      password:"",
      gender:"",
      email:"",
    }
  },
  methods:{
    validatePhone() {
    const phonePattern = /^\d{10}$/; 
    return phonePattern.test(this.phone);
    },
    register(){
      const userData = {
        username: this.username,
        password: this.password,
        name: this.name,
        phone: this.phone,
        gender: this.gender,
        email: this.email,
      };
      axios
      .post("/api/customer",userData)
      .then((res) => {
        alert(res.data.message);
        this.name = "";
        this.phone = "";
        this.username = "";
        this.password = "";
        this.gender = "";
        this.email = "";
      })
      .catch((error) => {
          console.error(error);
          alert("Register Fail,Please check python");
        });
    }
  }
};
</script>