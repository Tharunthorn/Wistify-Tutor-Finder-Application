import { createStore } from 'vuex';

const store = createStore({
    state: {
        loggedIn: false,
        user: {
            firstName: 'John', // Replace with actual user data
            lastName: 'Doe',   // Replace with actual user data
            accessToken: '1234567890', // Replace with actual user data
        },
    },
    mutations: {
        setLoggedIn(state, loggedIn) {
            state.loggedIn = loggedIn;
        },
    },
});

export default store;