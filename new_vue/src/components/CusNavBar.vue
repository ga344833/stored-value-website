<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container">
      
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-sm-0">
          <li class="nav-item">
            <a class="nav-link" aria-current="page">
              <router-link to="/">回登入頁面</router-link>
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" aria-current="page">
              <router-link to="/customer/homepage">主頁</router-link>
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" aria-current="page">
              <router-link to="/customer/users">客戶列表</router-link>
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" aria-current="page">
              <router-link to="/customer/products">商品列表</router-link>
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" aria-current="page">
              <router-link to="/customer/topuprecord">儲值紀錄</router-link>
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" aria-current="page">
              <router-link to="/customer/allpurchaserecord">購買紀錄</router-link>
            </a>
          </li>  
        </ul>
        <form class="d-flex">
          <input
            class="form-control me-2"
            type="search"
            placeholder="Search"
            aria-label="Search"
          />
          <button class="btn btn-outline-success" type="submit">Search</button>
        </form>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "CusNavBar",
};
</script>

<style scoped>
.router-link-active {
  text-decoration: none;
  color: #0460bd;
}
a {
  text-decoration: none;
  color: #93bbe6;
}

.nav-item{
  margin-right : 10px;
  margin-left : 10px;
}

</style>
