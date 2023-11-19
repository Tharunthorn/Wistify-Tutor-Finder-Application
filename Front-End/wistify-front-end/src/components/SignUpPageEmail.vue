<template>
  <NavBar />
  <div class="signup-page">
    <img class="background-image" src="public/Background_Blur.svg" alt="Background Image" />
    <div class="signup-box">
      <img class="logo" src="public/Logo_black.svg" alt="WISTIFY Logo" />
      <form @submit.prevent="submitForm" method="post">
        <input v-model="firstName" type="text" placeholder="First Name" class="signup-input" />
        <input v-model="lastName" type="text" placeholder="Last Name" class="signup-input" />
        <input v-model="emailAddress" type="email" placeholder="Email Address" class="signup-input" />
        <input v-model="password" type="password" placeholder="Password" class="signup-input" />
        <button type="submit" class="submit-button" >Submit</button>
      </form>
      <router-link to="/SignUp" class="back-button">Back</router-link>
    </div>
  </div>
</template>

<script>
import NavBar from "./NavBar.vue";
import axios from "axios";
import router from "../router/index.js";

export default {
  components: {NavBar},
  data() {
    return {
      firstName: '',
      lastName: '',
      emailAddress: '',
      password: ''
    };
  },
  methods: {
    async submitForm() {
      try {
        const response = await axios.post("http://127.0.0.1:8002/learner_sign_up/", {
          email: this.emailAddress,
          first_name: this.firstName,
          last_name: this.lastName,
          password: this.password,
        });

        console.log(response.data);
        router.push("/SignIn");
      } catch (error) {
        console.error(error)
      }
    }
  }
  // Add logic here if needed
}
</script>

<style scoped>
.signup-page {
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

.signup-box {
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

.signup-input {
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

.signup-input:focus {
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
</style>
