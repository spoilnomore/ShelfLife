<template>
  <div class="about-us">
    <h1>About Us</h1>
    <p>Welcome to ShelfLife!</p>
    <p>Our mission is to help households reduce food waste by keeping track of food items in an organized way. ShelfLife makes it easy for users to monitor expiration dates, manage pantry inventory, and share items within households.</p>
    <p>Whether you’re a student sharing a dorm pantry or a family managing a large household, ShelfLife provides a simple solution to reduce waste and save money.</p>

    <!-- Our Team Section -->
    <h2>Our Team</h2>
    <div class="team-container">
      <div class="team-member" v-for="member in teamMembers" :key="member.name">
        <img :src="member.image" :alt="`${member.name}'s picture`" class="team-image" />
        <h3>{{ member.name }}</h3>
        <p>{{ member.role }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AboutUs",
  data() {
    return {
      teamMembers: [
  {
    name: "Tomas Chavarria",
    role: "Frontend Developer",
    image: require("@/assets/tomas.png"), // Correct extension
  },
  {
    name: "Jacques Fleischer",
    role: "System Configuration Developer",
    image: require("@/assets/jp.png"), // Correct extension
  },
  {
    name: "Mikhail Vorotnikov",
    role: "Backend Developer and PM",
    image: require("@/assets/mikhail.png"), // Correct extension
  },
  {
    name: "Alejandro Fluitt Martinez",
    role: "QA and Scribe",
    image: require("@/assets/alex.png"), // Correct extension
  },
],

    };
  },
};
</script>

<style scoped>
.about-us {
  padding: 20px;
  max-width: 800px;
  margin: 0 auto;
  text-align: center;
}

h1 {
  margin-bottom: 20px;
}

h2 {
  margin-top: 40px;
}

p {
  margin-bottom: 15px;
  line-height: 1.6;
}

.team-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
  margin-top: 20px;
}

.team-member {
  text-align: center;
  max-width: 200px;
}

.team-image {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  object-fit: cover;
  margin-bottom: 10px;
}
</style>
