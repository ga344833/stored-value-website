<template>
  <div class="forgetpw-popup">
    <h2>忘記密碼</h2>
    <from @submit.prevent="forgetpw">
      <label for="username">請輸入帳號 : </label>
      <input type="text" id="username" v-model="formData.username" required />
      <br />
      <button type="submit">get password</button>
    </from>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      formData: {
        username: "",
      },
    };
  },
  methods: {
    forgetpw() {
      axios
        .post("/api/ForgetpwPopup", this.formData)
        .then((res) => {
          if (res.data.code === 0) {
            this.$emit("close");
            alert("您的密碼為" + res.data.message);
          } else {
            alert("該帳號尚未註冊，請確認後重試");
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
