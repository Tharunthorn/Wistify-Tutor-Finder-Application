<template>
  <NavBar />
  <div class="signup-page">
    <img class="background-image" src="public/Background_Blur.svg" alt="Background Image" />
    <div class="signup-box">
      <img class="logo" src="public/Logo_black.svg" alt="WISTIFY Logo" />
      <router-link to="/SignUpEmailTutor" class="signup-button email">EMAIL</router-link>
      <router-link to="/" class="signup-button google">GOOGLE</router-link>
      <!-- Your signup form content goes here -->
    </div>
  </div>
</template>

<script>
import NavBar from "./NavBar.vue";

export default {
  components: {NavBar}
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
  margin-bottom: 185px;
  /* Add more styling for your logo if needed */
}

.signup-button {
  text-align: center;
  font-family: 'Montserrat', sans-serif;
  width: 438px;
  height: 80px;
  background-color: #FFF;
  border: 5px solid #000;
  color: #000;
  font-size: 1.5rem;
  font-weight: bold;
  cursor: pointer;
  border-radius: 14px;
  margin-bottom: 30px;
  text-decoration: none; /* Remove underline */
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background-color 0.3s, color 0.3s;
}

.signup-button:hover {
  background-color: #000;
  color: #FFF;
}

.signup-button.email:hover {
  /* Additional styles for the EMAIL button on hover */
}

.signup-button.google:hover {
  /* Additional styles for the GOOGLE button on hover */
}
</style>
