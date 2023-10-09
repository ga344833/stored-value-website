<template>
  <div>
    <h1>客服界面</h1>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>姓名</th>
          <th>电话</th>
          <th>电子邮件</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="customer in customersData" :key="customer.id">
          <td>{{ customer.id }}</td>
          <td>{{ customer.fullname }}</td>
          <td>{{ customer.phone }}</td>
          <td>{{ customer.email }}</td>

          <router-link
            :to="{
              name: 'CustomerDetail',
              params: { customerId: customer.id, token: token },
            }"
          >
            個人資訊
          </router-link>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "UserPage",
  data() {
    return {
      customersData: [], // 存储从后端获取的客户数据
      token: "",
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
    fetchCustomersData() {
      // 使用Vue Resource或Axios等库从后端获取数据
      // 例如使用Vue Resource：

      // 获取 JWT 令牌，假设你的令牌存储在 Vuex 中或其他地方

      const headers = {
        Authorization: `Bearer ${this.token}`,
      };

      axios
        .get("/api/customers", { headers })
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
