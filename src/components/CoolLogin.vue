<template>
  <div class="login-page" :class="theme">
    <div class="login-container">
      <h1>Welcome to ShelfLife</h1>
      <p v-if="!showCreateForm && !showHouseholdOption">Please sign in to continue.</p>
      <b-button v-if="!showCreateForm && !showHouseholdOption" variant="primary" @click="signInWithGoogle">
        <font-awesome-icon :icon="['fab', 'google']" /> Sign in with Google
      </b-button>

      <!-- Ask for Username if the user is new -->
      <div v-if="showCreateForm && !showHouseholdOption">
        <b-form @submit.prevent="promptHousehold">
          <b-form-group label="Username">
            <b-form-input v-model="newUsername" required></b-form-input>
          </b-form-group>
          <b-button variant="primary" type="submit">Next</b-button>
        </b-form>
      </div>

      <!-- Ask to Join or Create Household -->
      <div v-if="showHouseholdOption && !showHouseholdInput">
        <p>Do you want to join a household or make a new one?</p>
        <b-button
          variant="success"
          @click="showJoinHouseholdInput"
          :disabled="!householdsAvailable"
          :title="!householdsAvailable ? 'No households available' : ''"
        >
          Join Household
        </b-button>
        <b-button variant="primary" @click="showCreateHouseholdInput">
          Create New Household
        </b-button>
      </div>


      <!-- Input for Joining Existing Household -->
      <div v-if="showHouseholdInput === 'join'">
        <b-form @submit.prevent="createUser(false)">
          <b-form-group label="Select a Household to Join">
            <b-form-select 
              v-model="selectedHouseholdId" 
              :options="householdOptions.length > 0 ? householdOptions : [{ value: null, text: 'No households available' }]" 
              required>
            </b-form-select>

          </b-form-group>
          <b-button variant="primary" type="submit">Join Household</b-button>
        </b-form>
      </div>


      <!-- Input for Creating New Household -->
      <div v-if="showHouseholdInput === 'create'">
        <b-form @submit.prevent="createUser(true)">
          <b-form-group label="Create New Household Name">
            <b-form-input v-model="newHouseholdName" required></b-form-input>
          </b-form-group>
          <b-button variant="primary" type="submit">Create Household</b-button>
        </b-form>
      </div>
    </div>
  </div>
</template>

<script>
import { auth, provider } from '../firebase';
import { signInWithPopup } from 'firebase/auth';

export default {
  name: 'CoolLogin',
  data() {
    return {
      theme: this.$root.theme,
      showCreateForm: false,
      showHouseholdOption: false,
      showHouseholdInput: null,
      newUsername: '',
      newHouseholdName: '',
      googleUser: null,
      householdOptions: [], // Array to store households fetched from backend
      selectedHouseholdId: null, // ID of the selected household
      householdsAvailable: false,
    };
  },
  methods: {
    async signInWithGoogle() {
      try {
        const result = await signInWithPopup(auth, provider);
        const user = result.user;
        const google_id = user.uid;
        const email = user.email;

        // Call backend to check if user exists
        const response = await fetch('http://localhost:8081/check-user', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ google_id, email }),
        });

        const data = await response.json();

        if (data.isNewUser || !data.user.household_name) {
          // User is new or doesn't have a household; prompt to complete setup
          this.googleUser = { google_id, email };
          this.showCreateForm = true;

          // Pre-fill username if it exists
          if (data.user && data.user.username) {
            this.newUsername = data.user.username;
          }
        } else {
          // Existing user with household, log them in and redirect
          localStorage.setItem('loggedInUser', data.user.username);
          localStorage.setItem('userHouseholdName', data.user.household_name);
          localStorage.setItem('householdId', data.user.household_id);

          this.$router.push('/');
        }

      } catch (error) {
        console.error('Error during sign-in:', error);
      }
    },
      promptHousehold() {
        if (!this.newUsername) return;
        this.showCreateForm = false;
        this.showHouseholdOption = true;

        // Fetch households to check availability
        this.fetchHouseholds();
      },

    showJoinHouseholdInput() {
      this.showHouseholdOption = false;
      this.showHouseholdInput = 'join';

      // Fetch households for the dropdown
      this.fetchHouseholds();
    },
    showCreateHouseholdInput() {
      this.showHouseholdOption = false;
      this.showHouseholdInput = 'create';
      
    },
    async fetchHouseholds() {
    try {
      const response = await fetch('http://localhost:8081/households', {
        method: 'GET',
      });
      const data = await response.json();
      console.log('Fetched households:', data);
      this.householdOptions = data.map(household => ({
        value: household.id,
        text: household.name || household.household_name,
      }));
      console.log('Household options:', this.householdOptions);

      // Update householdsAvailable based on fetched data
      this.householdsAvailable = this.householdOptions.length > 0;
    } catch (error) {
      console.error('Error fetching households:', error);
      this.householdsAvailable = false;
    }
  },

  async createUser(createNewHousehold) {
    if (!createNewHousehold && !this.selectedHouseholdId) {
      alert('Please select a household to join.');
      return;
    }

    const payload = {
      google_id: this.googleUser.google_id,
      email: this.googleUser.email,
      username: this.newUsername,
      household_name: createNewHousehold ? this.newHouseholdName : null,
      household_id: createNewHousehold ? null : this.selectedHouseholdId, // Ensure this is a number or string
      create_new_household: createNewHousehold,
    };

    console.log('Payload:', payload);

      try {
        const response = await fetch('http://localhost:8081/create-user', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(payload),
        });

        const data = await response.json();
        console.log('Response:', data); // Log response for debugging
        if (data.error) {
          alert(data.error);
          return;
        }

      // Save user info and redirect
      localStorage.setItem('loggedInUser', data.user.username);
      if (data.user.household_name) {
        localStorage.setItem('userHouseholdName', data.user.household_name);
        localStorage.setItem('householdId', data.user.household_id);
      }

      this.$router.push('/');

      } catch (error) {
        console.error('Error creating user:', error);
      }
    }


  },
  watch: {
  selectedHouseholdId(newValue) {
    console.log('Selected household ID:', newValue);
  },
},

};
</script>



<style scoped>
.login-page {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 80vh;
  flex-grow: 1;
}

.light .login-page {
    background-color: #ffffff;
    color: #000000;
}

.dark .login-page {
    background-color: #4c382c;
    color: #ffffff;
}

.login-container {
  text-align: center;
}

.light .login-container {
  background-color: #ffffff;
  color: #000000;
}

.dark .login-container {
  background-color: #4c382c;
  color: #ffffff;
}

.login-container {
    padding: 40px;
    border-radius: 8px;
}
</style>
