<template>
  <div>
    <h1>用戶界面</h1>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>姓名</th>
          <th>电话</th>
          <th>國家</th>
          <th>驗證種類</th>
          <th>驗證密碼</th>
          <th>驗證圖像</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="customer in customersData" :key="customer.id">
          <td>{{ customer.id }}</td>
          <td>{{ customer.fullname }}</td>
          <td>{{ customer.phone }}</td>
          <td>{{ customer.country }}</td>
          <td>{{ customer.idtype }}</td>
          <td>{{ customer.idnumber }}</td>
          <img
            :src="'data:image/png;base64,' + customer.profile_image"
            alt="Profile Image"
          />
        </tr>
      </tbody>
    </table>

    <!-- 输入字段和确认按钮 -->
    <div v-if="isEditing">
      <div>
        <label for="country">國家:</label>
        <input type="text" id="country" v-model="newCountry" />
      </div>
      <div>
        <label for="idtype">驗證種類:</label>
        <input type="text" id="idtype" v-model="newIdType" />
      </div>
      <div>
        <label for="idnumber">驗證密碼:</label>
        <input type="text" id="idnumber" v-model="newIdNumber" />
      </div>
      <button @click="saveData">保存</button>
    </div>

    <!-- 新增按钮 -->
    <button @click="isEditing = true" v-if="showAddProfile">
      新增個人資訊
    </button>
    |
    <button @click="uploadVerificationPhoto">上傳驗證照片</button>
    <input
      type="file"
      @change="handleFileChange"
      ref="fileInput"
      style="display: none"
    />
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      customersData: [], // 存储从后端获取的客户数据
      token: "",
      isEditing: false, // 控制是否显示输入字段和确认按钮
      newCountry: "", // 用于存储新的国家数据
      newIdType: "", // 用于存储新的验证类型数据
      newIdNumber: "", // 用于存储新的验证密码数据
      alertMessage: "", // 提醒视窗的消息
      showAddProfile: true,
    };
  },
  created() {
    // 在页面加载时获取客户数据，包括發送令牌JWT
    this.token = localStorage.getItem("token");
    if (this.token) {
      this.fetchCustomersData();
    } else {
      console.error("No valid token found.");
    }
  },
  methods: {
    // 新增方法以触发文件选择输入框的点击事件
    uploadVerificationPhoto() {
      this.$refs.fileInput.click(); // 触发文件选择输入框的点击事件
    },
    handleFileChange(event) {
      this.selectedPhoto = event.target.files[0];
      console.log("Selected photo:", this.selectedPhoto);
      const formData = new FormData();
      formData.append("file", this.selectedPhoto);

      const headers = {
        Authorization: `Bearer ${this.token}`,
      };
      axios
        .post("/api/customer/upload_image", formData, { headers })
        .then((response) => {
          // 处理上传成功的响应
          console.log("Photo upload response:", response.data);
          window.alert("驗證照片上傳成功！");
          window.location.reload();
        })
        .catch((error) => {
          // 处理上传失败的情况
          console.error("Error uploading photo:", error);
          window.alert("驗證照片上傳失敗。請稍後重試。");
        });
    },

    startEditing() {
      this.isEditing = true;
    },
    // 保存数据
    saveData() {
      const data = {
        country: this.newCountry,
        idtype: this.newIdType,
        idnumber: this.newIdNumber,
      };
      const headers = {
        Authorization: `Bearer ${this.token}`,
      };
      const userConfirmed = window.confirm("确定要保存个人资料吗？");

      if (userConfirmed) {
        axios
          .patch("/api/customer/profile", data, { headers })
          .then((response) => {
            this.customersData = response.data;
            console.log("Response from PATCH request:", response.data);
            // 根据您的需求将数据发送到后端
            // 在这里添加发送数据到后端的代码
            // 发送成功后，显示提醒视窗
            this.alertMessage = "資訊已儲存";
            // 保存成功后，清空输入字段并关闭编辑
            this.newCountry = "";
            this.newIdType = "";
            this.newIdNumber = "";
            this.isEditing = false;
            window.alert("个人资料已成功保存。");

            // 重新获取客户数据，如果需要的话
            this.fetchCustomersData();
          })
          .catch((error) => {
            console.error("Error fetching customer data:", error);
            this.alertMessage = "更新失败，请稍后重试";
          });
      }
    },
    fetchCustomersData() {
      // 使用Vue Resource或Axios等库从后端获取数据
      // 例如使用Vue Resource：

      // 获取 JWT 令牌，假设你的令牌存储在 Vuex 中或其他地方

      const headers = {
        Authorization: `Bearer ${this.token}`,
      };

      axios
        .get("/api/customer/profile", { headers })
        .then((response) => {
          this.customersData = response.data;
        })
        .catch((error) => {
          console.error("Error fetching customer data:", error);
        });
    },
  },
};
</script>

<style scoped>
/* 样式可以根据您的需求进行自定义 */
table {
  width: 100%;
  border-collapse: collapse;
}

th,
td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

th {
  background-color: #f2f2f2;
}
</style>
