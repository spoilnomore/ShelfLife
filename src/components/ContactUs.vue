<!-- src/components/ContactUs.vue -->
<template>
  <div id="contact-us">
        <h1>Contact Us</h1>
        <br>
        <p>We’d love to hear from you! If you have any questions, feedback, or suggestions, please reach out using the contact information below.</p> 
        <br>
        <ul>
          <li>Email: <a href="mailto:spoilnomore@hotmail.gov">spoilnomore@hotmail.gov</a></li>
          <li>Phone: <a href="tel:+1234567890">+1 (234) 567-890</a></li>
          <li>Address: 123 Pantry Lane, Food Town, FT 12345</li>
        </ul>
      <br>
  </div>
</template>
  
  <script>
  export default {
    name: "ContactUs",
  };
  </script>
  
  <style scoped>
  #contact-us {
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 20px;
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
  