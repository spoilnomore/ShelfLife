<!-- src/components/AboutUs.vue -->
<template>
    <div class="about-us">
      <h1>About Us</h1>
      <p>Welcome to ShelfLife!</p>
      <p>Our mission is to help households reduce food waste by keeping track of food items in an organized way. ShelfLife makes it easy for users to monitor expiration dates, manage pantry inventory, and share items within households.</p>
      <p>Whether you’re a student sharing a dorm pantry or a family managing a large household, ShelfLife provides a simple solution to reduce waste and save money.</p>
    </div>
  </template>
  
  <script>
  export default {
    name: "AboutUs",
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
  
  p {
    margin-bottom: 15px;
    line-height: 1.6;
  }
  </style>
  