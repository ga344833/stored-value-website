<template>
    <div class="PatchProductForm"></div>
    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#patchModal">
  編輯商品
</button>

<!-- Modal -->
<div class="modal fade" id="patchModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">編輯商品</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <form class="row g-3 needs-validation" novalidate>
  <div class="col-md-6">
    <label for="id" class="form-label">Id</label>
    <div class="input-group has-validation">
      <input type="text" class="form-control" id="username" aria-describedby="inputGroupPrepend" v-model="id" required>
      <div class="invalid-feedback">
        Please insert amount.
      </div>
    </div>
  </div>
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
  <div class="col-md-6">
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
        <button type="button" class="btn btn-primary" data-bs-dismiss="modal" @click="patchproduct">編輯</button>
      </div>
    </div>
  </div>
</div>
</template>
<script>
import axios from "axios";
export default {
  name: "PatchProductForm", 
  data(){
    return{
      id:"",
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
    patchproduct(){
      const productData = {
        id:this.id,
        name: this.name,
        price: this.price,
        amount: this.amount
      };
      const headers = {
        Authorization: `Bearer ${this.token}`,
      };
      axios
      .patch("/api/product/profile",productData,{ headers })
      .then((res) => {
        alert(res.data.message);
        this.id = "";
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