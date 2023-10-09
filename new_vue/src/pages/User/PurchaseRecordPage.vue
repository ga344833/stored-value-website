<template lang="html">
  <div class="cover"> 
      <p>PurchaseRecordPage</p>
  </div>
  <table class="table table-striped">
    <thead>
  <tr>
    <th scope="col">購買時間</th>
    <th scope="col">購買物品</th>
    <th scope="col">購買數量</th>
    <th scope="col">總價</th>
  </tr>
</thead>
<tbody>
  <tr v-for="product in productsData" :key="product.id">
      <th scope="row">{{ product.purchase_time }}</th>
      <td>{{ product.product_item }}</td>
      <td>{{ product.product_amount }}</td>
      <td>{{ product.total }}</td>
    </tr>
</tbody>
  </table>
</template>
<script>
import axios from "axios";
export default {
  name: "PurchaseRecordPage",
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
        .get("/api/purchases", { headers })
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
