import { createRouter, createWebHistory } from 'vue-router';
import LandingPage from "../components/LandingPage.vue";
import SignUpPage from "../components/SignUpPage.vue";
import SignUpPageEmail from "../components/SignUpPageEmail.vue";
import ExplorePage from "../components/ExplorePage.vue";


const routes = [
    {
        path: '/',
        name: 'LandingPage',
        component: LandingPage,
    },

    {
        path: '/SignUp',
        name: 'SignUp',
        component: SignUpPage,
    },

    {
        path: '/SignUpEmail',
        name: 'SignUpEmail',
        component: SignUpPageEmail,
    },

    {
        path: '/Explore',
        name: 'Explore',
        component: ExplorePage,
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;