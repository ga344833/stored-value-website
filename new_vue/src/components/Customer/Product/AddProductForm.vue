<template>
    <div class="AddProductForm"></div>
    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
  新增商品
</button>

<!-- Modal -->
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">新增商品</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <form class="row g-3 needs-validation" novalidate>
  <div class="col-md-6">
    <label for="name" class="form-label" >Name</label>
    <input type="text" class="form-control" id="name" v-model="name" required>
    <div class="valid-feedback">
      Please insert product name.
    </div>
  </div>
  <div class="col-md-6">
    <label for="price" class="form-label">Price</label>
    <input type="tel" class="form-control" id="phone" v-model="price" required>
    <div class="valid-feedback">
      Please insert product price.
    </div>
  </div>
  <div class="col-md-12">
    <label for="username" class="form-label">Amount</label>
    <div class="input-group has-validation">
      <input type="text" class="form-control" id="username" aria-describedby="inputGroupPrepend" v-model="amount" required>
      <div class="invalid-feedback">
        Please insert amount.
      </div>
    </div>
  </div>
</form>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">關閉</button>
        <button type="button" class="btn btn-primary" data-bs-dismiss="modal" @click="addproduct">註冊</button>
      </div>
    </div>
  </div>
</div>
</template>
<script>
import axios from "axios";
export default {
  name: "AddProductForm", 
  data(){
    return{
      name:"",
      price:"",
      amount:"",
      token: "",
    }
  },
  created() {
    this.token = localStorage.getItem("token");
  },
  methods:{
    addproduct(){
      const productData = {
        name: this.name,
        price: this.price,
        amount: this.amount
      };
      const headers = {
        Authorization: `Bearer ${this.token}`,
      };
      axios
      .post("/api/product/create",productData,{ headers })
      .then((res) => {
        alert(res.data.message);
        this.name = "";
        this.price = "";
        this.amount = "";
        window.location.reload(); 
      })
      .catch((error) => {
          console.error(error);
          alert("Register Fail,Please check python");
        });
    }
  }
};
</script>