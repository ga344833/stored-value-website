<template lang="">
  <p></p>
  <CustomerCard :showCards="showCards"></CustomerCard>
</template>
<script>
import CustomerCard from "../../components/CustomerCard.vue";
export default {
  name: "CustomerhomePage",
  components:{
      CustomerCard,
  },
  data() {
    return {
      showCards: true,
    };
  },
};
</script>
<style></style>