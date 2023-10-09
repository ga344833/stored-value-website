<template lang="">
    <div class="cover"> 
        <p>login as customer</p>
    </div>
    <CusNavBar></CusNavBar>
    <div class="container">
        <router-view></router-view>
    </div>
    <p></p>
    
    
    <!--1.當前用戶總數-->
    <!--2.客戶須審核人數-->
    <!--3.銀行卡須審核人數-->
    <!--4.帳戶-->
</template>
<script>
import CusNavBar from "../../components/CusNavBar.vue";
export default {
  name: "CustomerPage",
  components:{
      CusNavBar,
  },
  data() {
    return {
      showCards: true,
    };
  },
};
</script>
<style></style>