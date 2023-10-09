<template lang="html">
    <div class="cover"> 
        <p>ProductviewPage</p>
    </div>
    <table class="table table-striped">
      <thead>
    <tr>
      <th scope="col">ID</th>
      <th scope="col">Name</th>
      <th scope="col">Price</th>
      <th scope="col">Amount</th>
    </tr>
  </thead>
  <tbody>
    <tr v-for="product in productsData" :key="product.id">
        <th scope="row">{{ product.id }}</th>
        <td>{{ product.name }}</td>
        <td>{{ product.price }}</td>
        <td>{{ product.amount }}</td>
      </tr>
  </tbody>
  <p></p>
    </table>
    <div class="container">
      <div class="row">
    <div class="col">
      <AddProductForm></AddProductForm>
    </div>
    <div class="col">
      <PatchProductForm></PatchProductForm>
    </div>
    <div class="col">
      <DeleteProductForm></DeleteProductForm>
    </div>
  </div>
</div>
</template>
<script>
import axios from "axios";
import AddProductForm from "@/components/Customer/Product/AddProductForm.vue";
import PatchProductForm from "@/components/Customer/Product/PatchProductForm.vue";
import DeleteProductForm from "@/components/Customer/Product/DeleteProductForm.vue";
export default {
    data() {
  return {
    productsData: [],
    token: "",
  };
},
components: {
  AddProductForm,
  PatchProductForm,
  DeleteProductForm,
  },
created() {
    this.token = localStorage.getItem("token");
    if (this.token) {
      this.fetchProductsData();
    } else {
      console.error("No valid token found.");
    }
  },
  methods: {
    fetchProductsData() {
      const headers = {
        Authorization: `Bearer ${this.token}`,
      };
      axios
        .get("/api/products", { headers })
        .then((response) => {
          this.productsData = response.data.allinfo;
        })
        .catch((error) => {
          console.error("Error fetching product data:", error);
        });
    },
  },
};
</script>
<style></style>