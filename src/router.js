import { createRouter, createWebHistory } from 'vue-router'
import AddFood from './components/AddFood.vue'
import UserLogin from './components/Login.vue'

const routes = [
    { path: '/add', component: AddFood },
    { path: '/login', component: UserLogin }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router