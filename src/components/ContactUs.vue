<!-- src/components/ContactUs.vue -->
<template>
  <div :class="contact-us">
      <div class="text-div">
        <h1>Contact Us</h1>
      </div>
      <div class="text-div">
        <p>We’d love to hear from you! If you have any questions, feedback, or suggestions, please reach out using the contact information below.</p>
      </div>
      <div class="text-div">  
        <ul>
          <li>Email: <a href="mailto:spoilnomore@hotmail.gov">spoilnomore@hotmail.gov</a></li>
          <li>Phone: <a href="tel:+1234567890">+1 (234) 567-890</a></li>
          <li>Address: 123 Pantry Lane, Food Town, FT 12345</li>
        </ul>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "ContactUs",
  };
  </script>
  
  <style scoped>
  .contact-us {
    padding: 20px;
    max-width: 600px;
    margin: 0 auto;
    display: flex;
    flex-grow: 1;
  }

  .text-div {
    padding: 20px;
    justify-content: center;
    text-align: center;
  }
  
  h1 {
    margin-bottom: 20px;
    align-items: center;
  }
  
  ul {
    list-style: none;
    padding: 0;
    align-items: center;
  }
  
  li {
    margin-bottom: 10px;
    align-items: center;
  }
  
  a {
    color: #007bff;
    text-decoration: none;
    align-items: center;
  }
  
  a:hover {
    text-decoration: underline;
  }
  </style>
  