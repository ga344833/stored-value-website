<template>
  <div class="login">
    <h1>Login</h1>
    <el-input v-model="username" placeholder="Username"></el-input>
    <el-input
      v-model="password"
      placeholder="Password"
      type="password"
    ></el-input>
    <el-button @click="login" type="primary">Login</el-button> |
    <el-button @click="showRegisterPopup" type="primary">Register</el-button> |
    <el-button @click="showForgetpwPopup" type="primary"
      >forget password</el-button
    >
    <register-popup
      v-if="isRegisterPopupVisible"
      @close="closeRegisterPopup"
    ></register-popup>
    <forgetpw-popup
      v-if="isForgetpwPopupVisible"
      @close="closeForgetpwPopup"
    ></forgetpw-popup>
  </div>
</template>

<script>
import axios from "axios";
import RegisterPopup from "@/components/RegisterPopup.vue";
import ForgetpwPopup from "@/components/ForgetpwPopup.vue";

export default {
  name: "LoginPage",
  data() {
    return {
      isRegisterPopupVisible: false,
      isForgetpwPopupVisible: false,
      username: "",
      password: "",
    };
  },
  components: {
    RegisterPopup,
    ForgetpwPopup,
  },
  methods: {
    showRegisterPopup() {
      this.isRegisterPopupVisible = true;
    },
    closeRegisterPopup() {
      this.isRegisterPopupVisible = false;
    },
    showForgetpwPopup() {
      this.isForgetpwPopupVisible = true;
    },
    closeForgetpwPopup() {
      this.isForgetpwPopupVisible = false;
    },
    login() {
      const userData = {
        username: this.username,
        password: this.password,
      };
      axios
        .post("/api/login", userData)
        .then((res) => {
          if (res.data.code === 0) {
            // 登录成功，你可以在这里进行相应的页面跳转或其他操作
            localStorage.setItem("token", res.data.token);
            this.$router.push({
              name: "dashboard",
            });
          }
          if (res.data.code === 2) {
            alert("Login failed");
          }
          if (res.data.code === 1) {
            localStorage.setItem("token", res.data.token);
            this.$router.push({
              name: "internal",
            });
          }
        })
        .catch((error) => {
          console.error(error);
          alert("Login failed");
        });
    },
  },
};
</script>
