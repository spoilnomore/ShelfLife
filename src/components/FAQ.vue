<!-- src/components/FAQ.vue -->
<template>
    <div class="faq">
      <h1>Frequently Asked Questions</h1>
      <ul>
        <li>
          <h3>What is ShelfLife?</h3>
          <p>ShelfLife is a food management app designed to help households reduce waste by keeping track of food expiration dates and managing pantry inventory.</p>
        </li>
        <li>
          <h3>How can I add a new food item?</h3>
          <p>You can add a new food item by navigating to the "Add Food" page and filling out the required details.</p>
        </li>
        <li>
          <h3>How can I delete an expired food item?</h3>
          <p>Go to the "View Foods" page, locate the item you want to delete, and click the "Delete" button next to it.</p>
        </li>
        <li>
          <h3>How do I change the theme?</h3>
          <p>You can toggle between light and dark themes by clicking the sun/moon icon in the top right corner of the page.</p>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: "FAQ",
  };
  </script>
  
  <style scoped>
  .faq {
    padding: 20px;
    max-width: 800px;
    margin: 0 auto;
    text-align: left;
    font-size: 0.9rem; /* Small font size */
  }
  
  h1 {
    text-align: center; /* Center the title */
    margin-bottom: 20px;
  }
  
  ul {
    list-style: none; /* Removes bullets or numbering */
    padding-left: 1.5em; /* Optional: adds indentation */
  }
  
  li {
    margin-bottom: 15px;
  }
  
  h3 {
    font-weight: bold;
    margin: 0; /* Align heading closely with the paragraph */
  }
  
  p {
    margin: 5px 0 0;
    line-height: 1.5;
  }
  </style>
  