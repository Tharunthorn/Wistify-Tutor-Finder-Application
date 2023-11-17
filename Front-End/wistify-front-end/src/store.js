import { createStore } from 'vuex';

const store = createStore({
  state: {
    loggedIn: false,
    user: {
      id: null,
      email: null,
      firstName: null,
      lastName: null,
    },
  },
  mutations: {
    setLoggedIn(state, loggedIn) {
      state.loggedIn = loggedIn;
    },
    setUser(state, userData) {
      state.user.id = userData.id;
      state.user.email = userData.email;
      state.user.firstName = userData.first_name;
      state.user.lastName = userData.last_name;
    },
    initializeStore(state) {
      // Check if there's a token in local storage
      const token = localStorage.getItem('token');
      if (token) {
        state.loggedIn = true;

        const user = JSON.parse(localStorage.getItem('user'));
        if (user) {
          state.user = user;
        }
      }
    },
  },
  actions: {
    login({ commit }, { token, user }) {
      // Save the token in local storage
      localStorage.setItem('token', token);

      // Save the user details in local storage
      localStorage.setItem('user', JSON.stringify(user));

      // Commit mutations to update state
      commit('setLoggedIn', true);
      commit('setUser', user);
    },
    logout({ commit }) {
      // Remove the token and user details from local storage
      localStorage.removeItem('token');
      localStorage.removeItem('user');

      // Commit mutations to update state
      commit('setLoggedIn', false);
      commit('setUser', {
        id: null,
        email: null,
        firstName: null,
        lastName: null,
      });
    },
  },
});

export default store;
