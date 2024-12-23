import { createRouter, createWebHistory } from 'vue-router';
import AddFood from './components/AddFood.vue';
import UserLogin from './components/CoolLogin.vue';
import CoolPantry from './components/CoolPantry.vue'; // Main pantry component
import FAQ from '@/components/FAQ.vue';
import ContactUs from '@/components/ContactUs.vue';
import AboutUs from '@/components/AboutUs.vue';

const routes = [
  {
    path: '/',
    name: 'CoolPantry',
    component: CoolPantry,
    meta: {
      requiresAuth: true,
      title: 'Pantry - ShelfLife',
    },
  },
  {
    path: '/faq',
    name: 'FAQ',
    component: FAQ,
    meta: {
      title: 'FAQ - ShelfLife',
    },
  },
  {
    path: '/about',
    name: 'AboutUs',
    component: AboutUs,
    meta: {
      title: 'About Us - ShelfLife',
    },
  },
  {
    path: '/contact',
    name: 'ContactUs',
    component: ContactUs,
    meta: {
      title: 'Contact Us - ShelfLife',
    },
  },
  {
    path: '/add',
    name: 'AddFood',
    component: AddFood,
    meta: {
      requiresAuth: true,
      title: 'Add Food - ShelfLife',
    },
  },
  {
    path: '/login',
    name: 'Login',
    component: UserLogin,
    meta: {
      title: 'Login - ShelfLife',
    },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// Navigation guard to check for authenticated users and set document title
router.beforeEach((to, from, next) => {
  const loggedInUser = localStorage.getItem('loggedInUser');
  const householdName = localStorage.getItem('userHouseholdName');

  // Set the document title based on the route meta title
  if (to.meta && to.meta.title) {
    document.title = to.meta.title;
  }

  // Check if the route requires authentication
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (!loggedInUser || !householdName) {
      // User is not authenticated or hasn't completed setup
      next('/login');
    } else {
      // User is authenticated and has completed setup
      next();
    }
  } else {
    // Route does not require authentication
    next();
  }
});

export default router;
