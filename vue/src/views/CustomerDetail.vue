<template>
  <div>
    <h2>客户資訊</h2>
    <div>
      <p><strong>ID:</strong> {{ customer.id }}</p>
      <p><strong>姓名:</strong> {{ customer.fullname }}</p>
      <p><strong>電話:</strong> {{ customer.phone }}</p>
      <p><strong>電子郵件:</strong> {{ customer.email }}</p>
      <p><strong>國家:</strong> {{ customer.country }}</p>
      <p><strong>驗證種類:</strong> {{ customer.idtype }}</p>
      <p><strong>驗證密碼:</strong> {{ customer.idnumber }}</p>
      <p><strong>驗證圖檔:</strong></p>
      <img
        :src="'data:image/png;base64,' + customer.profile_image"
        alt="Profile Image"
      />
      <p><strong>審核狀態:</strong>{{ customer.state }}</p>
      <button @click="approveCustomer">審核通過</button> |
      <button @click="rejectCustomer">審核拒絕</button>
    </div>
  </div>
  <h2>銀行卡資訊</h2>
  <p><strong>user_ID:</strong> {{ bankCards.user_id }}</p>
  <p><strong>銀行:</strong> {{ bankCards.bank }}</p>
  <p><strong>卡號:</strong> {{ bankCards.card_number }}</p>
  <p><strong>驗證圖檔:</strong></p>
  <img
    :src="'data:image/png;base64,' + bankCards.card_image"
    alt="Profile Image"
  />
  <p><strong>審核狀態:</strong> {{ bankCards.state }}</p>
  <button @click="approveBankcard">審核通過</button> |
  <button @click="rejectBankcard">審核拒絕</button>
  <h2>自身帳戶資訊</h2>
  <p><strong>帳戶:</strong> {{ accountInfo.account_number }}</p>
  <p><strong>餘額:</strong> {{ accountInfo.balance }}</p>
</template>

<script>
import axios from "axios";

export default {
  props: {
    customerId: String, // 确保类型匹配客户 ID 的类型
  },
  data() {
    return {
      customer: {}, // 存储客户详细信息
      bankCards: {},
      accountInfo: {},
      token: "",
    };
  },
  created() {
    this.token = localStorage.getItem("token");

    if (this.token) {
      this.fetchCustomerDetail();
    } else {
      console.error("No valid token found.");
    }

    const customerId = this.$route.params.customerId; // 从路由参数中获取客户的ID
    this.fetchCustomerDetail(customerId);
  },
  methods: {
    fetchCustomerDetail(customerId) {
      // 使用客户的ID从后端获取客户详细信息
      // 你需要根据你的后端 API 进行调整
      const headers = {
        Authorization: `Bearer ${this.token}`,
      };

      axios
        .get(`/api/customer/${customerId}`, { headers }) // 假设你的 API 端点是 /api/customer/:id
        .then((response) => {
          this.customer = response.data;
          axios
            .get(`/api/bankcard/${customerId}`, { headers }) // 假设你的 API 端点是 /api/bankcard/:customer_id
            .then((response) => {
              this.bankCards = response.data;
              axios
                .get(`/api/account/${customerId}`, { headers })
                .then((response) => {
                  this.accountInfo = response.data; // 更新自身帳戶資訊
                })
                .catch((error) => {
                  console.error("Error fetching account info:", error);
                });
            })
            .catch((error) => {
              console.error("Error fetching bank card detail:", error);
            });
        })
        .catch((error) => {
          console.error("Error fetching customer detail:", error);
        });
    },
    // 審核通過
    approveCustomer() {
      const confirmApproval = window.confirm("確認審核通過嗎？");
      if (confirmApproval) {
        this.updateCustomerState("approved");
      }
    },
    approveBankcard() {
      const confirmApproval = window.confirm("確認審核通過嗎？");
      if (confirmApproval) {
        this.updateBankcardState("approved");
      }
    },

    // 審核拒絕
    rejectCustomer() {
      const confirmRejection = window.confirm("確認審核拒絕嗎？");
      if (confirmRejection) {
        this.updateCustomerState("rejected");
      }
    },
    rejectBankcard() {
      const confirmRejection = window.confirm("確認審核拒絕嗎？");
      if (confirmRejection) {
        this.updateBankcardState("rejected");
      }
    },

    // 更新客户状态的方法
    updateCustomerState(newState) {
      const headers = {
        Authorization: `Bearer ${this.token}`,
      };
      const customerId = this.customer.id;

      axios
        .patch(
          `/api/customer/${customerId}/verify`,
          { state: newState },
          { headers }
        )
        .then((response) => {
          if (response.data.success) {
            alert("審核狀態已更新！");
            // 審核成功後重新加載客戶詳細信息
            this.fetchCustomerDetail(customerId);
          } else {
            alert("無法更新審核狀態。");
          }
        })
        .catch((error) => {
          console.error("Error updating customer state:", error);
          alert("無法更新審核狀態。請稍後再試。");
        });
    },
    updateBankcardState(newState) {
      const headers = {
        Authorization: `Bearer ${this.token}`,
      };
      const customerId = this.customer.id;

      axios
        .patch(
          `/api/bankcard/${customerId}/verify`,
          { state: newState },
          { headers }
        )
        .then((response) => {
          if (response.data.success) {
            alert("審核狀態已更新！");
            // 審核成功後重新加載客戶詳細信息
            this.fetchCustomerDetail(customerId);
          } else {
            alert("無法更新審核狀態。");
          }
        })
        .catch((error) => {
          console.error("Error updating customer state:", error);
          alert("無法更新審核狀態。請稍後再試。");
        });
    },
  },
};
</script>

<style scoped>
/* 样式可以根据您的需求进行自定义 */
</style>
