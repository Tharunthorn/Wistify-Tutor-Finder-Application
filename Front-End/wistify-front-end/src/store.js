import { createStore } from 'vuex';
import axios from 'axios';

const store = createStore({
  state: {
    loggedIn: false,
    user: null,
  },
  mutations: {
    setLoggedIn(state, loggedIn) {
      state.loggedIn = loggedIn;
    },
    setUser(state, user) {
      state.user = user;
    },
  },
  actions: {
    async fetchUser({ commit }) {
      try {
        const token = localStorage.getItem('token');
        if (token) {
          const response = await axios.get('http://localhost:8000/get_learner/', {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          });

          commit('setUser', response.data);
          commit('setLoggedIn', true);
        }
      } catch (error) {
        console.error(error);
      }
    },
  },
});

export default store;
