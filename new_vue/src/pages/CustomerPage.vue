<template lang="">
    <div class="cover"> 
        <p>login as customer</p>
    </div>
    <CusNavBar></CusNavBar>
    <div class="container">
        <router-view></router-view>
    </div>
</template>
<script>
import CusNavBar from "../components/CusNavBar.vue"
export default {
  name: "CustomerPage",
  components:{
      CusNavBar
  }
};
</script>
<style></style>