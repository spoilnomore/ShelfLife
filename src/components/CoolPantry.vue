<!-- src/components/Pantry.vue -->
<template>
  <div class="pantry" :class="$root.theme">
    <b-table striped hover :items="foods" :fields="fields"></b-table>
  </div>
</template>

<script>
export default {
  name: 'CoolPantry',
  data() {
    return {
      foods: [
        { id: 1, name: 'Apple', category: 'Fruit', quantity: 10 },
        { id: 2, name: 'Bread', category: 'Grain', quantity: 5 },
        { id: 3, name: 'Carrot', category: 'Vegetable', quantity: 7 },
        { id: 4, name: 'Chicken', category: 'Meat', quantity: 4 },
      ],
      fields: ['id', 'name', 'category', 'quantity'],
    };
  },
};
</script>

<style scoped>
/* ... your styles ... */
</style>
