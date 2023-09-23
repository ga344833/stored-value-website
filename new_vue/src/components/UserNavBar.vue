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
              <router-link to="/">Main</router-link>
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" aria-current="page">
              <router-link to="/user/intro">簡介</router-link>
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" aria-current="page">
              <router-link to="/user/info">個人資料</router-link>
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
  name: "UserNavBar",
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
