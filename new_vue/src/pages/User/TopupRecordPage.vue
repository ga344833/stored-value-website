<template lang="html">
  <div class="cover"> 
      <p>TopupRecordPage</p>
  </div>
  <table class="table table-striped">
    <thead>
  <tr>
    <th scope="col">儲值帳戶</th>
    <th scope="col">儲值金額</th>
    <th scope="col">儲值時間</th>
    <th scope="col">餘額紀錄</th>
  </tr>
</thead>
<tbody>
  <tr v-for="record in recordsData" :key="record.id">
      <th scope="row">{{ record.account_number }}</th>
      <td>{{ record.topup_balance }}</td>
      <td>{{ record.topup_time }}</td>
      <td>{{ record.user_balance }}</td>
    </tr>
</tbody>
  </table>
</template>
<script>
import axios from "axios";
export default {
  name: "TopupRecordPage",
  data() {
  return {
    recordsData: [],
    token: "",
  };
},
  created() {
    this.token = localStorage.getItem("token");
    if (this.token) {
      this.fetchData();
    } else {
      console.error("No valid token found.");
    }
  },
  methods:{
    fetchData(){
      const headers = {
        Authorization: `Bearer ${this.token}`,
      };
      axios
        .get("/api/account/topup_record", { headers })
        .then((response) => {
          this.recordsData = response.data.allinfo;
        })
        .catch((error) => {
          console.error("Error fetching product data:", error);
        });
    }
  }
};

</script>
<style></style>
