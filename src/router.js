import { createRouter, createWebHistory } from 'vue-router'
import AddFood from './components/AddFood.vue'


const routes = [
    { path: '/add', component: AddFood }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router