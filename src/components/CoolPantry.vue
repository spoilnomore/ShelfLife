<template>
  <div class="pantry" :class="$root.theme">
    <!-- Household name display -->
    <div class="household-header">
      <h2>{{ householdName }}</h2>
    </div>

    <b-table :items="foods" :fields="fields" striped hover responsive>
      <template #cell(expiration_date)="data">
        <span :class="{ 'text-danger': isPastDate(data.item.expiration_date) }">
          {{ formatDate(data.item.expiration_date) }}
        </span>
      </template>
      <template #cell(sharing)="data">
        <span :class="getSharingClass(data.item.sharing)">
          {{ data.item.sharing }}
        </span>
      </template>

      <template #cell(image)="data">
        <div v-if="data.item.image">
          <img :src="data.item.image" alt="Food Image" class="food-image" />
        </div>
        <div v-else>
          <span>No Image</span>
        </div>
      </template>

      <template #cell(actions)="data">
        <b-button variant="danger" size="sm" @click="deleteFood(data.item.id, data.item.title)">Delete</b-button>
      </template>
    </b-table>
  </div>
</template>

<script>
import axios from 'axios';
import { BTable, BButton } from 'bootstrap-vue-next';
import $ from 'jquery';

export default {
  name: 'CoolPantry',
  components: {
    BTable,
    BButton,
  },
  data() {
    return {
      householdName: localStorage.getItem('userHouseholdName') || 'Unknown Household',
      foods: [],
      fields: [
        { key: 'id', label: 'ID' },
        { key: 'title', label: 'Food Name' },
        { key: 'location', label: 'Location' },
        { key: 'owner', label: 'Owner' },
        { key: 'expiration_date', label: 'Expiration Date' },
        { key: 'sharing', label: 'Sharing' },
        { key: 'image', label: 'Image' },
        { key: 'actions', label: 'Actions' },
      ],
    };
  },
  computed: {
    serverUrl() {
      return process.env.VUE_APP_SERVER_URL;
    },
  },
  async created() {
    await this.fetchFoods();
    this.$nextTick(() => {
      // Initialize DataTable on created
      $('#pantryTable').DataTable({
        paging: true,
        searching: true,
        autoWidth: true,
        responsive: true,
        dom: 'Bfrtip',
        buttons: ['copy', 'excel', 'pdf', 'print'],
      });
    });
  },
  methods: {
    // Fetch all food items from the backend
    async fetchFoods() {
  const householdId = localStorage.getItem('householdId');
  if (!householdId) {
    console.error('householdId is missing in localStorage');
    return;
  }

  try {
    const response = await fetch(`http://localhost:8081/foods?household_id=${householdId}`);
    const data = await response.json();

    // Prepend server URL to image paths
    const serverUrl = process.env.VUE_APP_SERVER_URL || 'http://localhost:8081';
    this.foods = data.map(food => ({
  ...food,
  image: food.image_location
    ? (food.image_location.startsWith('http') ? food.image_location : `${serverUrl}/uploads/${food.image_location}`)
    : null,
}));

    // Debugging: Log the transformed foods array
    console.log('Fetched foods (mapped):', this.foods);
  } catch (error) {
    console.error('Error fetching foods:', error);
  }
}
    ,
    // Format date to make it more readable
    formatDate(dateString) {
      const options = { year: 'numeric', month: 'long', day: 'numeric' };
      return new Date(dateString).toLocaleDateString(undefined, options);
    },
    // Check if the expiration date has passed
    isPastDate(date) {
      const today = new Date();
      today.setHours(0, 0, 0, 0);
      return new Date(date) < today;
    },
    // Get class based on sharing value
    getSharingClass(sharing) {
      switch (sharing) {
        case 'Yes': return 'text-success';
        case 'No': return 'text-danger';
        case 'Ask me': return 'text-warning';
        default: return 'text-muted';
      }
    },
    // Delete a food item
    async deleteFood(foodId, foodTitle) {
      if (confirm(`Are you sure you want to delete ${foodTitle}?`)) {
        try {
          await axios.delete(`http://localhost:8081/foods/${foodId}`);
          this.foods = this.foods.filter(food => food.id !== foodId);
        } catch (error) {
          console.error("Failed to delete food:", error);
        }
      }
    },
  },
};
</script>

<style scoped>
.household-header {
  display: flex;
  justify-content: center; 
  align-items: center;   
  text-align: center;    
}
.pantry {
  padding: 20px;
}
.b-table tr:hover {
  background-color: #f8f9fa !important;
  transition: background-color 0.3s;
}
.text-danger {
  color: red;
}
.text-success {
  color: green;
}
.text-warning {
  color: orange;
}
.text-muted {
  color: gray;
}
.pantry .table {
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.food-image {
  max-width: 100px; /* Limit the width */
  max-height: 100px; /* Limit the height */
  object-fit: cover; /* Keep aspect ratio */
  border-radius: 4px; /* Optional: Add rounded corners */
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1); /* Optional: Add a slight shadow */
}
</style>
