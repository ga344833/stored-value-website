<template lang="html">
  <div class="cover"> 
    <p>userviewPage</p>
  </div>
  <table class="table table-striped">
    <thead>
      <tr>
        <th scope="col">ID</th>
        <th scope="col">Name</th>
        <th scope="col">Phone</th>
        <th scope="col">Email</th>
        <th scope="col">Register time</th>
        <th scope="col">State</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="customer in customersData" :key="customer.id">
        <th scope="row">{{ customer.id }}</th>
        <td>{{ customer.fullname }}</td>
        <td>{{ customer.phone }}</td>
        <td>{{ customer.email }}</td>
        <td>{{ customer.register_time }}</td>
        <td>
          <router-link :to="{name:'UserDetailPage', params:{customerId:customer.id,token:token}}">
            {{ customer.state }}
          </router-link>
        </td>
      </tr>
    </tbody>
  </table>
</template>
<script>
import axios from "axios";

export default {
  name: "UserviewPage",
    data() {
  return {
    customersData: [],
    waitingData: [],
      token: "",
  };
},
created() {
    this.token = localStorage.getItem("token");
    if (this.token) {
      this.fetchCustomersData();
    } else {
      console.error("No valid token found.");
    }
  },
  methods: {
    fetchCustomersData() {
      const headers = {
        Authorization: `Bearer ${this.token}`,
      };
      axios
        .get("/api/customers", { headers })
        .then((response) => {
          this.customersData = response.data.allinfo;
          this.waitingData = response.data.waitinginfo;
        })
        .catch((error) => {
          console.error("Error fetching customer data:", error);
        });
    },
  },
};
</script>
<style></style>