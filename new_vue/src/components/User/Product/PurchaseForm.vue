<template>
    <div class="PurchaseForm"></div>
    <button type="button" class="btn btn-primary" data-bs-toggle="modal" :data-bs-target="'#PurchaseModal-' + product.id" @click="beforecreate">
  購買商品
</button>

<!-- Modal -->
<div class="modal fade" :id="'PurchaseModal-' + product.id" tabindex="-1" aria-labelledby="PurchaseModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="PurchaseModalLabel">購買商品</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <form class="row g-3 needs-validation" novalidate>
  <div class="col-md-6">
    <label for="name" class="form-label" >商品名稱:{{product.name}}</label>
    <div class="valid-feedback">
      Please insert product name.
    </div>
  </div>
  <div class="col-md-6">
    <label for="price" class="form-label">價格:{{product.price}}</label>
    <div class="valid-feedback">
      Please insert product price.
    </div>
  </div>
  <div class="col-md-6">
    <label for="price" class="form-label">剩餘數量:{{product.amount}}</label>
    <div class="valid-feedback">
      Please insert product price.
    </div>
  </div>
  <div class="col-md-6">
    <label for="price" class="form-label">帳戶餘額:{{account_balance}}</label>
    <div class="valid-feedback">
      Please insert product price.
    </div>
  </div>
  <div class="col-md-6">
    <label for="username" class="form-label">選擇購買數量:</label>
    <div class="input-group has-validation">
      <select class="form-select" id="validationCustom04" v-model="amount" required>
      <option selected disabled value="">數量 :</option>
      <option>1</option>
      <option>2</option>
      <option>3</option>
      <option>4</option>
      </select>
      <div class="invalid-feedback">
        Please insert amount.
      </div>
    </div>
  </div>
  <div class="col-md-6">
    <label for="price" class="form-label">合計金額 : {{totalAmount}} </label>
    <div class="valid-feedback">
      Please insert product price.
    </div>
  </div>
</form>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">關閉</button>
        <button type="button" class="btn btn-primary" data-bs-dismiss="modal" @click="purchase">確定</button>
      </div>
    </div>
  </div>
</div>
</template>
<script>
import axios from "axios";
export default {
  name: "PurchaseForm", 
  props: {
    product: Object,
    account_balance:Number,
  },
  data(){
    return{
      token: "",
      amount: 1,
    }
  },
  created() {
    this.token = localStorage.getItem("token");
  },
  computed:{
      totalAmount(){
        return this.amount * this.product.price;
      }
  },
  methods:{
    purchase(){
      const productData = {
        product_item: this.product.name,
        product_amount: this.amount,
        total: this.totalAmount,
      };
      const headers = {
        Authorization: `Bearer ${this.token}`,
      };
      if (this.account_balance >= this.totalAmount)
      {
        console.log("product_item : "+this.product.name);
        console.log("stock : "+this.product.amount);
        console.log("total : "+this.totalAmount);
        if (this.product.amount > 0){
      axios
      .post("/api/purchases/process",productData,{ headers })
      .then((res) => {
        console.log('客戶扣款完成、商品庫存扣除');
        axios
        .post("/api/purchases/new",res.data,{ headers })
        console.log('建立購買紀錄');
        alert("購買完成");
        window.location.reload(); 
      })
      .catch((error) => {
          console.error(error);
          alert("Register Fail,Please check python");
        });
      }
      else{
        alert("庫存不足，請等待進貨");
        window.location.reload(); 
      }
    }
      else{
        alert("餘額不足，請進行儲值後再進行購買");
        window.location.reload(); 
      }
    }
  }
};
</script>