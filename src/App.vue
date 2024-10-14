<template>
  <div id="app" :class="theme">
    <b-navbar toggleable="lg" :style="{ backgroundColor: `var(--${theme}-navbar-background)`, color: `var(--${theme}-navbar-text-color)` }">
      <b-navbar-brand to="/">
        <font-awesome-icon icon="kitchen-set" style="padding-left: 10px;" /> ShelfLife
      </b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav class="me-auto">
          <b-nav-item to="/">View Foods</b-nav-item>
          <b-nav-item to="/add">Add Food</b-nav-item>
        </b-navbar-nav>
      </b-collapse>

      <b-navbar-nav class="ml-auto">
        <b-nav-item v-if="loggedInUser" to="/claim">
          <div class="claim-button">
            Claim Food
            <span class="notification-bubble" v-if="claimableFoodsCount > 0">{{ claimableFoodsCount }}</span>
          </div>
        </b-nav-item>
        <b-nav-item v-if="loggedInUser">
          <span class="nav-link">Hi, {{ loggedInUser }}</span>
          <b-button variant="link" @click="logout">Sign Out</b-button>
        </b-nav-item>
        <b-nav-item v-else to="/login">Login</b-nav-item>
        <b-nav-item>
          <b-button variant="link" @click="toggleTheme">
            <font-awesome-icon :icon="theme === 'dark' ? faSun : faMoon" />
          </b-button>
        </b-nav-item>
      </b-navbar-nav>
    </b-navbar>

    <!-- Dummy Data Table -->
    <b-table striped hover :items="foods" :fields="fields"></b-table>
    <router-view @add-food="addFood" :foods="foods" />
  </div>
</template>

<script>
import { faSun, faMoon, faKitchenSet } from '@fortawesome/free-solid-svg-icons';

export default {
  name: 'App',
  data() {
    return {
      foods: [
        { id: 1, name: 'Apple', category: 'Fruit', quantity: 10 },
        { id: 2, name: 'Bread', category: 'Grain', quantity: 5 },
        { id: 3, name: 'Carrot', category: 'Vegetable', quantity: 7 },
        { id: 4, name: 'Chicken', category: 'Meat', quantity: 4 },
      ],
      fields: ['id', 'name', 'category', 'quantity'], // Table columns
      theme: 'light',
      faSun,
      faMoon,
      faKitchenSet,
      loggedInUser: localStorage.getItem('loggedInUser'),
      claimableFoodsCount: 0,
    };
  },
  methods: {
    toggleTheme() {
      this.theme = this.theme === 'dark' ? 'light' : 'dark';
    },
    logout() {
      localStorage.removeItem('loggedInUser');
      this.loggedInUser = null;
      this.$router.push('/login');
    },
  },
  mounted() {
    this.theme = 'dark'; // Set initial theme
  },
};
</script>


<style>
:root {
  --light-navbar-text-color: black;
  --dark-navbar-text-color: white;
  --light-navbar-toggler-color: black;
  --dark-navbar-toggler-color: white;
  --light-navbar-background: #f4e1d2;
  --dark-navbar-background: #3e2723;
  /* dark mocha */
  --light-navbar-brand-color: #000000;
  /* or whatever color you want in light mode */
  --dark-navbar-brand-color: #d3d3d3;
  /* light grey */
  --light-background: #ffffff;
  --light-text: #000000;

  --dark-background: #4c382c;
  --dark-text: #ffffff;
}

.light {
  background-color: var(--light-background);
  color: var(--light-text);
}

.dark {
  background-color: var(--dark-background);
  color: var(--dark-text);
}


.dark .navbar-nav .nav-link,
.dark .navbar-brand {
  color: var(--dark-navbar-text-color) !important;
}

.light .navbar-nav .nav-link,
.light .navbar-brand {
  color: var(--light-navbar-text-color) !important;
}

.right-align {
  text-align: right;
}

.claim-button {
  position: relative;
  display: inline-block;
}

.notification-bubble {
  position: absolute;
  top: 0;
  right: 0;
  transform: translate(90%, -50%);
  display: inline-block;
  background-color: red;
  color: white;
  border-radius: 50%;
  padding: 2px 8px;
}
.navbar-toggler {
    color: var(--light-navbar-toggler-color);
}

.dark .navbar-toggler {
    color: var(--dark-navbar-toggler-color);
}

.navbar-toggler-icon {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 30 30'%3E%3Cpath stroke='rgba(0, 0, 0, 1)' stroke-linecap='round' stroke-miterlimit='10' stroke-width='2' d='M4 7h22M4 15h22M4 23h22'/%3E%3C/svg%3E");
}

.dark .navbar-toggler-icon {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 30 30'%3E%3Cpath stroke='rgba(255, 255, 255, 1)' stroke-linecap='round' stroke-miterlimit='10' stroke-width='2' d='M4 7h22M4 15h22M4 23h22'/%3E%3C/svg%3E");
}
</style>
