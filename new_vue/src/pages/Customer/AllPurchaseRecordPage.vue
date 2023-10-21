<template lang="html">
  <div class="cover"> 
      <p>AllPurchaseRecordPage</p>
  </div>
  <table class="table table-striped">
    <thead>
  <tr>    
    <th scope="col">購買時間</th>
    <th scope="col">用戶姓名</th>
    <th scope="col">購買物品</th>
    <th scope="col">購買數量</th>
    <th scope="col">總價</th>
    <th scope="col">用戶當前餘額</th>
    <th scope="col">用戶購買後餘額</th>
  </tr>
</thead>
<tbody>
  <tr v-for="product in productsData" :key="product.id">
      <th scope="row">{{ product.purchase_time }}</th>
      <td>{{ product.buyer }}</td>
      <td>{{ product.product_item }}</td>
      <td>{{ product.product_amount }}</td>
      <td>{{ product.total }}</td>
      <td>{{ product.buyer_balance }}</td>
      <td>{{ product.after_purchase_balance }}</td>
    </tr>
</tbody>
  </table>
</template>
<script>
import axios from "axios";
export default {
  name: "AllPurchaseRecordPage",
  data() {
  return {
    productsData: [],
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
        .get("/api/purchases/all", { headers })
        .then((response) => {
          this.productsData = response.data.PurchaseRecords;
        })
        .catch((error) => {
          console.error("Error fetching product data:", error);
        });
    }
  }
};

</script>
<style></style>
