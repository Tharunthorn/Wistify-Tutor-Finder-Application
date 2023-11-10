import { createRouter, createWebHistory } from 'vue-router';
import LandingPage from "../components/LandingPage.vue";
import ProfilePage from "../components/ProfilePage.vue";


const routes = [
    {
        path: '/',
        name: 'LandingPage',
        component: LandingPage,
    },
    {
        path: '/Profile',
        name: 'ProfilePage',
        component: ProfilePage,
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;