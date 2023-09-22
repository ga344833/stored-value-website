<template>
  <div>
    <h1>用戶界面</h1>
    <!-- 用戶詳細信息 -->
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

    <!-- 銀行卡信息 -->
    <h2>銀行卡資訊</h2>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>銀行</th>
          <th>卡號</th>
          <th>狀態</th>
          <th>圖片</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="card in bankCards" :key="card.id">
          <td>{{ card.id }}</td>
          <td>{{ card.bank }}</td>
          <td>{{ card.card_number }}</td>
          <td>{{ card.state }}</td>
          <img
            :src="'data:image/png;base64,' + card.card_image"
            alt="Profile Image"
          />
        </tr>
      </tbody>
    </table>
  </div>

  <div v-if="showAddBankCardForm">
    <label for="cardNumber">卡号：</label>
    <input type="text" id="cardNumber" v-model="newBankCard.card_number" />

    <label for="bank">银行：</label>
    <input type="text" id="bank" v-model="newBankCard.bank" />

    <button @click="addBankCard">保存银行卡</button>
  </div>

  <button @click="showAddBankCardForm = true">新增银行卡</button> |
  <button @click="uploadBankcardImage">上傳銀行卡照片</button>
  <input
    type="file"
    @change="handleBankCardFileChange"
    ref="fileInput"
    style="display: none"
  />
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      customersData: [], // 存储从后端获取的客户数据
      bankCards: [], // 存储从后端获取的銀行卡數據
      token: "",
      isEditing: false, // 控制是否显示输入字段和确认按钮
      newCountry: "", // 用于存储新的国家数据
      newIdType: "", // 用于存储新的验证类型数据
      newIdNumber: "", // 用于存储新的验证密码数据
      alertMessage: "", // 提醒视窗的消息
      showAddProfile: true,
      showAddBankCardForm: false,
      newBankCard: {
        card_number: "",
        bank: "",
      },
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
    uploadBankcardImage() {
      this.$refs.fileInput.click(); // 触发文件选择输入框的点击事件
    },

    // 当用户选择文件后触发的事件处理函数
    handleBankCardFileChange(event) {
      const selectedPhoto = event.target.files[0];
      if (!selectedPhoto) return; // 用户取消选择文件

      // 创建一个FormData对象来包装文件
      const formData = new FormData();
      formData.append("file", selectedPhoto);

      // 发送文件到后端API
      const headers = {
        Authorization: `Bearer ${this.token}`,
      };
      axios
        .post("/api/bankcard/upload_image", formData, { headers })
        .then((response) => {
          // 处理上传成功的响应
          console.log("Photo upload response:", response.data);
          window.alert("銀行卡照片上傳成功！");
          window.location.reload(); // 刷新页面，或根据需要执行其他操作
        })
        .catch((error) => {
          // 处理上传失败的情况
          console.error("Error uploading bankcard photo:", error);
          window.alert("銀行卡照片上傳失敗。請稍後重試。");
        });
    },

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
      // 获取客户数据
      axios
        .get("/api/customer/profile", { headers })
        .then((response) => {
          this.customersData = response.data;
          // 获取銀行卡數據
          axios // 多執行緒同時跑，會導致token同時呼叫當機，要包在裡面跑才能運行
            .get("/api/bankcard/profile", { headers })
            .then((response) => {
              this.bankCards = response.data;
            })
            .catch((error) => {
              console.error("Error fetching bank card data:", error);
            });
        })
        .catch((error) => {
          console.error("Error fetching customer data:", error);
        });
    },
    addBankCard() {
      const headers = {
        Authorization: `Bearer ${this.token}`,
      };

      axios
        .post("/api/bankcard/create", this.newBankCard, { headers })
        .then((response) => {
          if (response.data.success) {
            // 添加成功的处理逻辑，例如显示成功消息，刷新银行卡列表等
            window.alert("银行卡信息已成功保存。");
            // 可以选择刷新银行卡列表
            this.fetchCustomersData();
          } else {
            // 添加失败的处理逻辑，例如显示错误消息
            window.alert(response.data.message);
          }
        })
        .catch((error) => {
          console.error("Error adding bank card:", error);
          window.alert("添加银行卡信息时发生错误，请稍后重试。");
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
