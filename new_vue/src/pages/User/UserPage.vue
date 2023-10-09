<template lang="html">
    <div class="cover"> 
        <p>login as user</p>
    </div>
    <UserNavBar></UserNavBar>
    <div class="container">
        <router-view></router-view>
    </div>
</template>
<script>
import UserNavBar from "@/components/UserNavBar.vue";
export default {
  name: "UserPage",
  components:{
      UserNavBar
  }
};
</script>
<style></style>