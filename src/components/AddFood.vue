<template>
    <div id="main">
        <h1>Add a new food item</h1>
        <form @submit.prevent="addFood">
            <div class="mb-3">
                <label for="title">Title:</label>
                <input id="title" v-model="newFood.title" required>
            </div>

            <div class="mb-3">
                <label for="location">Location:</label>
                <select id="location" v-model="newFood.location" required>
                    <option>Fridge Door Top Rack</option>
                    <option>Fridge Door Middle Rack</option>
                    <option>Fridge Door Bottom Rack</option>
                </select>
            </div>

            <div class="mb-3">
            <label for="owner">Owner:</label>
            <select id="owner" v-model="newFood.owner" required>
                <option v-for="member in householdMembers" :key="member.id" :value="member.username">
                {{ member.username }}
                </option>
                <option value="Unknown">Unknown</option>
            </select>
            </div>


            <div class="mb-3">
                <label for="expiration_date">Expiration Date:</label>
                <input id="expiration_date" type="date" v-model="newFood.expiration_date" required>
            </div>

            <div class="mb-3">
                <label for="sharing">Sharing:</label>
                <select id="sharing" v-model="newFood.sharing" required>
                    <option value="Yes">Yes</option>
                    <option value="No">No</option>
                    <option value="Ask me">Ask me</option>
                    <option value="Unknown">Unknown</option>
                </select>
            </div>

            <div class="mb-3">
                <label for="image">Image:</label>
                <input id="image" type="file" ref="fileInput" @change="onFileChange" accept=".jpg, .jpeg, .png, .gif">
            </div>

            <button type="submit" class="btn btn-primary" :disabled="isUploading">
                <span v-if="isUploading">
                    <font-awesome-icon icon="spinner" pulse /> Loading...
                </span>
                <span v-else>
                    Add Food
                </span>
            </button>
        </form>
    </div>
</template>
<script>
import axios from 'axios';

export default {
    data() {
        return {
            newFood: {
                title: '',
                location: '',
                owner: 'Unknown',
                expiration_date: '',
                sharing: 'Unknown', // New property for sharing
                image: null
            },
            fileInput: null, // New property
            isUploading: false,
            householdMembers: [],
        }
    },
    methods: {
        onFileChange(e) {
            this.newFood.image = e.target.files[0];
        },
        async addFood() {
            this.isUploading = true;
            let formData = new FormData();
            Object.keys(this.newFood).forEach(key => {
                formData.append(key, this.newFood[key]);
            });


            // Append household_id from localStorage
            const householdId = localStorage.getItem('householdId');
            if (!householdId) {
                throw new Error('Household ID is missing. Please try logging in again.');
            }
            formData.append('household_id', householdId);

            await axios.post('http://localhost:8081/foodAdd', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            });
            window.alert('mmm ShelfLife appreciates your delectable food');

            // Reset the form
            this.newFood = {
                title: '',
                location: '',
                owner: 'Unknown',
                expiration_date: '',
                sharing: 'Unknown',
                image: null
            };
            this.$refs.fileInput.value = ''; // Clear the file input field
            this.isUploading = false;
        },
        async fetchHouseholdMembers() {
            const householdId = localStorage.getItem('householdId');
            if (!householdId) {
            alert('Household ID is missing. Please try logging in again.');
            return;
            }

            try {
            const response = await axios.get(`http://localhost:8081/households/${householdId}/members`);
            this.householdMembers = response.data.members;
            } catch (error) {
            console.error('Error fetching household members:', error);
            alert('Error fetching household members.');
            }
        },
    },
    mounted() {
        this.fetchHouseholdMembers();
    },

}
</script>

<style scoped>
#main {
    text-align: center;
    justify-content: center;
    align-items: center;
    padding: 20px;
}

.mb3 {
    padding: 20px;
}
</style>