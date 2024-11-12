<!-- src/components/FAQ.vue -->
<template>
    <div class="faq">
      <h1>Frequently Asked Questions</h1>
      <p>If you have more questions, feel free to reach out to us!</p>
      <ul>
        <li>
          <h3>How can I contact ShelfLife support?</h3>
          <p>Email us at <a href="mailto:spoilnomore@hotmail.gov">spoilnomore@hotmail.gov</a></p>
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
    margin-bottom: 15px;
  }
  
  h3 {
    font-weight: bold;
  }
  
  a {
    color: #007bff;
    text-decoration: none;
  }
  
  a:hover {
    text-decoration: underline;
  }
  </style>
  