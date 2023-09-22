<template>
  <div class="register-popup">
    <h2>用户註冊</h2>
    <!-- 注册表单 -->
    <form @submit.prevent="register">
      <label for="fullname">Full Name:</label>
      <input type="text" id="fullname" v-model="formData.fullname" required />
      <br />
      <label for="phone">Phone:</label>
      <input type="text" id="phone" v-model="formData.phone" required />
      <br />
      <label for="email">email:</label>
      <input type="text" id="email" v-model="formData.email" required />
      <br />
      <label for="username">Username:</label>
      <input type="text" id="username" v-model="formData.username" required />
      <br />
      <label for="password">Password:</label>
      <input
        type="password"
        id="password"
        v-model="formData.password"
        required
      />
      <br />
      <label for="gender">Gender:</label>
      <select id="gender" v-model="formData.gender" required>
        <option value="male">Male</option>
        <option value="female">Female</option>
      </select>
      <br />
      <button type="submit">Register</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      formData: {
        fullname: "",
        phone: "",
        email: "",
        username: "",
        password: "",
        gender: "",
        internal: "0",
      },
    };
  },
  methods: {
    register() {
      // 在这里处理注册逻辑，发送注册请求给后端
      // 成功后可以关闭弹窗或进行其他操作
      axios
        .post("/api/users", this.formData)
        .then((res) => {
          if (res.data.success) {
            this.$emit("close");
            alert("注册成功");
          } else {
            alert("注册失败：" + res.data.message);
          }
        })
        .catch((error) => {
          console.error(error);
          alert("An error occurred");
        });
    },
  },
};
</script>

<style scoped>
/* 样式可以根据你的需求自定义 */
</style>
