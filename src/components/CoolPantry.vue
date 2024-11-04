<template>
  <div class="pantry" :class="$root.theme">
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
      foods: [],
      fields: [
        { key: 'id', label: 'ID' },
        { key: 'title', label: 'Food Name' },
        { key: 'location', label: 'Location' },
        { key: 'owner', label: 'Owner' },
        { key: 'expiration_date', label: 'Expiration Date' },
        { key: 'sharing', label: 'Sharing' },
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
      try {
        const response = await axios.get(`http://localhost:8081/foods`);
        this.foods = response.data;
      } catch (error) {
        console.error("Error fetching foods:", error);
      }
    },
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
</style>
