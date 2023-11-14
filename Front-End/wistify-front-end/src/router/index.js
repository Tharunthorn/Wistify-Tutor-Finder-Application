import { createRouter, createWebHistory } from 'vue-router';
import LandingPage from "../components/LandingPage.vue";
import ProfilePage from "../components/ProfilePage.vue";
import SignUpPage from "../components/SignUpPage.vue";
import SignUpPageEmail from "../components/SignUpPageEmail.vue";
import ExplorePage from "../components/ExplorePage.vue";
import SignInPage from "../components/SignInPage.vue";
import SignInPageEmail from "../components/SignInPageEmail.vue";
import TutorSignUpPage from "../components/TutorSignUpPage.vue";
import TutorSignUpPageEmail from "../components/TutorSignUpPageEmail.vue";
import TutorSignUpTagSelectionPage from "../components/TutorSignUpTagSelectionPage.vue";


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
        path: '/SignUpTutor',
        name: 'SignUpTutor',
        component: TutorSignUpPage,
    },

    {
        path: '/SignUpEmailTutor',
        name: 'SignUpEmailTutor',
        component: TutorSignUpPageEmail,
    },

    {
        path: '/SignUpTutorTagsSelection',
        name: 'SignUpTutorTagSelection',
        component: TutorSignUpTagSelectionPage,
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