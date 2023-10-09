<template lang="">
  <p>UserhomePage</p>
  <UserCard :showCards="showCards"></UserCard>
</template>
<script>
import UserCard from "../../components/UserCard.vue";
export default {
  name: "UserhomePage",
  components:{
      UserCard,
  },
  data() {
    return {
      showCards: true,
    };
  },
};
</script>
<style></style>