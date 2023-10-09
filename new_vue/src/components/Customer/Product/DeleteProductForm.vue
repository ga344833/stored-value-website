<template>
    <div class="DeleteProductForm"></div>
    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#deleteModal">
  移除商品
</button>

<!-- Modal -->
<div class="modal fade" id="deleteModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">移除商品</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <form class="row g-3 needs-validation" novalidate>
  <div class="col-md-12">
    <label for="name" class="form-label" >Name</label>
    <input type="text" class="form-control" id="name" v-model="name" required>
    <div class="valid-feedback">
      Please insert product name.
    </div>
  </div>
</form>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">關閉</button>
        <button type="button" class="btn btn-primary" data-bs-dismiss="modal" @click="deleteproduct">確定</button>
      </div>
    </div>
  </div>
</div>
</template>
<script>
import axios from "axios";
export default {
  name: "DeleteProductForm", 
  data(){
    return{
      name:"",
      token: "",
    }
  },
  created() {
    this.token = localStorage.getItem("token");
  },
  methods:{
    deleteproduct(){
      const productData = {
        name: this.name,
      };
      const headers = {
        Authorization: `Bearer ${this.token}`,
      };
      axios
      .delete("/api/product/delete",productData,{ headers })
      .then((res) => {
        alert(res.data.message);
        this.name = "";
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