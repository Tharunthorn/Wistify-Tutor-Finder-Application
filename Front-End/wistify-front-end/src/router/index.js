import { createRouter, createWebHistory } from 'vue-router';
import LandingPage from "../components/LandingPage.vue";
import SignUpPage from "../components/SignUpPage.vue";
import SignUpPageEmail from "../components/SignUpPageEmail.vue";
import ExplorePage from "../components/ExplorePage.vue";
import SignInPage from "../components/SignInPage.vue";
import SignInPageEmail from "../components/SignInPageEmail.vue";


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
        path: '/SignIn',
        name: 'SignIn',
        component: SignInPage,
    },

    {
        path: '/SignInEmail',
        name: 'SignInEmail',
        component: SignInPageEmail,
    },

    {
        path: '/Explore',
        name: 'Explore',
        props: true,
        component: ExplorePage,
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;