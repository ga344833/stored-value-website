<template>
  <div id="app">
    <div class="text-center my-3">
      <div class="header-container">
        <h2>johney simulation shit</h2>
      </div>
      <div class="container">
            <router-view></router-view>
      </div>
    </div>

    <div class="fixed-bottom">
      <footer class="bg-light text-center text-lg-center">
        <div class="footer-container">
          © 2023 Copyright: francischi.com
        </div>
      </footer>
    </div>

  </div>
</template>

<script>

export default {
  name: "App",
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #013e7b;
  margin-top: 60px;
}

.footer-container {
  position: relative;
  padding-bottom: 40px;
}
.fixed-bottom {
  position: absolute;
  width: 100%;
  bottom: 0;
}

.header-container {
  position: relative;
  padding-bottom : 2%;
}
</style>
