// src/router.js
import { createRouter, createWebHistory } from 'vue-router';
import AddFood from './components/AddFood.vue';
import UserLogin from './components/CoolLogin.vue';
import CoolPantry from './components/CoolPantry.vue'; // Main pantry component
import { auth } from './firebase';

const routes = [
    {
        path: '/',
        name: 'CoolPantry',
        component: CoolPantry,
        meta: { requiresAuth: true },
    },
    {
        path: '/add',
        name: 'AddFood',
        component: AddFood,
        meta: { requiresAuth: true },
    },
    {
        path: '/login',
        name: 'Login',
        component: UserLogin,
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

// Navigation guard to check for authenticated users
router.beforeEach((to, from, next) => {
    const user = auth.currentUser || localStorage.getItem('loggedInUser');

    if (to.matched.some((record) => record.meta.requiresAuth)) {
        if (!user) {
            next('/login');
        } else {
            next();
        }
    } else {
        next();
    }
});

export default router;
