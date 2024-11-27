<template>
  <div id="app" :class="theme">
    <!-- Main Content -->
    <main class="main-content">
      <div id="header">
        <b-navbar toggleable="lg"
                  :style="{
                    backgroundColor: `var(--${theme}-navbar-background)`,
                    color: `var(--${theme}-navbar-text-color)`
                  }">
          <b-navbar-brand to="/">
            <font-awesome-icon icon="kitchen-set" style="padding-left: 10px;" /> ShelfLife
          </b-navbar-brand>

          <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

          <b-collapse id="nav-collapse" is-nav>
            <b-navbar-nav class="me-auto">
              <b-nav-item v-if="loggedInUser" to="/">View Foods</b-nav-item>
              <b-nav-item v-if="loggedInUser" to="/add">Add Food</b-nav-item>
            </b-navbar-nav>

            <!-- Right-aligned Navbar Items -->
            <b-navbar-nav class="ml-auto">
              <!-- Send Reminders Button -->
              <b-nav-item v-if="loggedInUser">
                <b-button variant="warning" @click="sendReminders">Send Reminders</b-button>
              </b-nav-item>

              <!-- User Greeting and Logout -->
              <b-nav-item v-if="loggedInUser">
                <span class="nav-link">Hi, {{ loggedInUser }}</span>
                <b-button variant="link" @click="logout">Sign Out</b-button>
              </b-nav-item>

              <!-- Login Link -->
              <b-nav-item v-else to="/login">Login</b-nav-item>

              <!-- Theme Toggle Button -->
              <b-nav-item>
                <b-button variant="link" @click="toggleTheme">
                  <font-awesome-icon :icon="theme === 'dark' ? faSun : faMoon" />
                </b-button>
              </b-nav-item>
            </b-navbar-nav>
          </b-collapse>
        </b-navbar>
      </div>

      <router-view />

      <!-- Footer -->
      <div id="footer">
        <b-navbar toggleable="lg"
                  :style="{
                    backgroundColor: `var(--${theme}-navbar-background)`,
                    color: `var(--${theme}-navbar-text-color)`
                  }">

          <b-navbar-nav class="footer-links">
            <b-nav-item to="/help">Help</b-nav-item>
            <b-nav-item to="/contact">Contact</b-nav-item>
            <b-nav-item to="/faq">FAQ</b-nav-item>
            <b-nav-item to="/about">About Us</b-nav-item>
          </b-navbar-nav>
        </b-navbar>
      </div>
    </main>
  </div>
</template>


<script>
import { faSun, faMoon, faKitchenSet } from '@fortawesome/free-solid-svg-icons';
import { auth } from './firebase';
import { onAuthStateChanged, signOut } from 'firebase/auth';

export default {
  name: 'App',
  data() {
    return {
      theme: 'light',
      faSun,
      faMoon,
      faKitchenSet,
      loggedInUser: null,
    };
  },
  methods: {
    toggleTheme() {
      this.theme = this.theme === 'dark' ? 'light' : 'dark';
    },
    async logout() {
      try {
        await signOut(auth);
        localStorage.clear(); // Clear all localStorage data
        this.loggedInUser = null;
        this.$router.push('/login');
      } catch (error) {
        console.error('Error signing out:', error);
      }
    },
    async sendReminders() {
      try {
        const idToken = await auth.currentUser.getIdToken();

        const response = await fetch('http://localhost:8081/send-reminders', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${idToken}`,
          },
        });

        const data = await response.json();

        if (response.ok) {
          alert(data.message);
        } else {
          alert(`Error: ${data.error || 'Unable to send reminders'}`);
        }
      } catch (error) {
        console.error('Error sending reminders:', error);
        alert('An error occurred while sending reminders.');
      }
    },
  },
  created() {
    this.theme = 'dark'; // Set initial theme
    this.loggedInUser = localStorage.getItem('loggedInUser');

    // Listen for auth state changes
    onAuthStateChanged(auth, (user) => {
      if (user) {
        // Firebase user is logged in
        this.loggedInUser = user.displayName;
        localStorage.setItem('loggedInUser', user.displayName);

        // Optionally, get and store the access token for authenticated requests
        user.getIdToken().then((token) => {
          localStorage.setItem('accessToken', token);
        });
      } else {
        // User is logged out
        this.loggedInUser = null;
        localStorage.removeItem('loggedInUser');
        localStorage.removeItem('accessToken'); // Remove access token
        localStorage.removeItem('userHouseholdName');
        localStorage.removeItem('householdId');
      }
    });
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

.main-content {
    display: flex;
    flex-direction: column;
    flex-grow: 1;
    min-height: 100vh; /*92.75*/
}

.footer {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background-color: var(--footer-background-color, #f8f9fa);
    color: var(--footer-text-color, #333);
    display: flex;
    justify-content: center;
}

.footer-links {
    display: flex;
    justify-content: center; /* Centers the links horizontally */
    width: 100%;
}

.footer-links .nav-item a {
    color: inherit;
    text-decoration: none;
    }

.footer-links .nav-item a:hover {
    text-decoration: underline;
}
</style>
