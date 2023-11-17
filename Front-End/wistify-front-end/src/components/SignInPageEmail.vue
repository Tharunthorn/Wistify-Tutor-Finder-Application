<template>
  <div>
    <NavBar />
    <div class="signin-page">
      <img class="background-image" src="public/Background_Blur.svg" alt="Background Image" />
      <div class="signin-box">
        <h1 class="signin-title">Welcome Back</h1>
          <input v-model="emailAddress" type="email" placeholder="Email Address" class="signin-input" />
          <input v-model="password" type="password" placeholder="Password" class="signin-input" />
          <button @click="submitForm" class="submit-button">SignIn</button>
        <router-link to="/SignIn" class="back-button">Back</router-link>
        <!-- Display error message if there's an error -->
        <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import NavBar from "./NavBar.vue";
import axios from "axios";

export default {
  components: { NavBar },
  data() {
    return {
      emailAddress: '',
      password: '',
      errorMessage: '',
    };
  },
  methods: {
    async submitForm() {
      try {
        const response = await axios.post("http://localhost:8000/log_in/", {
          email: this.emailAddress,
          password: this.password,
        });

        const { token, user } = response.data;

        localStorage.setItem("token", token);

        this.$store.commit('setLoggedIn', true);
        this.$store.commit('setUser', user);

        this.$router.push("/");

      } catch (error) {
        console.error(error);
        this.errorMessage = "Invalid email or password. Please try again.";
      }
    },
  },
};
</script>

<style scoped>
.signin-page {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;
}

.background-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.signin-box {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 537px;
  height: 714px;
  background-color: #FFF;
  border: 2.5px solid #B8E830;
  border-radius: 24px;
  filter: drop-shadow(0px 4px 34px rgba(0, 0, 0, 0.30));
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.logo {
  width: 394.279px;
  height: 64.681px;
  margin-bottom: 50px;
  /* Add more styling for your logo if needed */
}

.signin-input {
  width: 438px;
  height: 30px;
  padding: 10px;
  margin-bottom: 30px;
  font-family: 'Montserrat', sans-serif;
  font-weight: 400;
  font-size: 16px;
  border: 2px solid #000000;
  border-radius: 7px;
}

.signin-input:focus {
  outline: none;
  border-color: #B8E830;
}

.submit-button {
  width: 438px;
  height: 50px;
  background-color: #B8E830;
  color: #FFF;
  font-size: 1.5rem;
  font-weight: bold;
  cursor: pointer;
  border-radius: 14px;
  margin-bottom: 15px;
  transition: background-color 0.3s, color 0.3s;
}

.submit-button:hover {
  background-color: #000;
}

.back-button {
  text-align: center;
  font-family: 'Montserrat', sans-serif;
  width: 438px;
  height: 50px;
  background-color: #FFF;
  border: 2px solid #000;
  color: #000;
  font-size: 1.5rem;
  font-weight: bold;
  cursor: pointer;
  border-radius: 14px;
  text-decoration: none;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 15px;
  transition: background-color 0.3s, color 0.3s;
}

.back-button:hover {
  background-color: #000;
  color: #FFF;
}

.signin-title {
  font-family: 'Gochi Hand', cursive;
  font-size: 4rem;
  margin-bottom: 100px;
}

.error-message {
  color: red;
  margin-top: 10px;
}
</style>
