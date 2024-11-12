<!-- src/components/ContactUs.vue -->
<template>
    <div class="contact-us">
      <h1>Contact Us</h1>
      <p>We’d love to hear from you! If you have any questions, feedback, or suggestions, please reach out using the contact information below.</p>
      <ul>
        <li>Email: <a href="mailto:spoilnomore@hotmail.gov">spoilnomore@hotmail.gov</a></li>
        <li>Phone: <a href="tel:+1234567890">+1 (234) 567-890</a></li>
        <li>Address: 123 Pantry Lane, Food Town, FT 12345</li>
      </ul>
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
    text-align: center;
  }
  
  h1 {
    margin-bottom: 20px;
  }
  
  ul {
    list-style: none;
    padding: 0;
  }
  
  li {
    margin-bottom: 10px;
  }
  
  a {
    color: #007bff;
    text-decoration: none;
  }
  
  a:hover {
    text-decoration: underline;
  }
  </style>
  