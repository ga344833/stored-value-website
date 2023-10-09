<template lang="">
    <div class="cover"> 
        <h3>用戶登入</h3>
        <p></p>
        帳號 : <input v-model="username" id="username" placeholder="Username">
        <br>
        <p></p>
        密碼 : <input v-model="password" id="password" placeholder="Password" type="password">
    <br>
    <p></p>
     
    </div>
    <div class="container">
  <div class="row">
    <div class="col">
      <button type="primary" class="btn btn-primary" @click="login">登入</button>
</div>
<div class="col">
  <RegisterForm></RegisterForm>
</div>
<div class="col">
  <a href="#" class="btn btn-primary">忘記密碼</a>
</div>
</div>
</div>
<p></p>
</template>
<script>
import axios from "axios";
import RegisterForm from "@/components/RegisterForm.vue";
export default {
  name: "LoginPage",
  data(){
    return{
        username:"",
        password:"",
    };
  },
  components: {
    RegisterForm,
  },
  methods:{
    login() {
      const userData = {
        username: this.username,
        password: this.password,
      };
      axios
        .post("/api/login", userData)
        .then((res) => {
          if (res.data.code === 0){
            localStorage.setItem("token",res.data.token);
            this.$router.push({
              name: "UserhomePage",
            });
          }
          if (res.data.code === 2) {
            alert("Login failed");
          }
          if (res.data.code === 1) {
            localStorage.setItem("token", res.data.token);
            this.$router.push({
              name: "CustomerhomePage",
            });
          }
        })
        .catch((error) => {
          console.error(error);
          alert("Login failed");
        });
  }},
};
</script>
<style></style>
