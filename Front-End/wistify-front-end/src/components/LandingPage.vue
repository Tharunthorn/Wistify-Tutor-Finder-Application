<template>
  <NavBar />
  <div class="hero-section">
    <div class="hero-content">
      <div class="search-container">
        <div class="hero-section-heading">
          Unlock Infinite Learning <br>
          Discover Your <span class="highlight-font">Tutor</span> Today
        </div>
        <div class="search-bar-container">
          <input type="text" class="search-bar" placeholder="Search for any subject..." />
          <button class="search-button"></button>
        </div>
        <div class="popular-options">
          <span class="popular-label">Popular:</span>
          <button v-for="option in popularOptions" :key="option" :class="['popular-option', getButtonWidth(option)]">{{ option }}</button>
        </div>
      </div>
    </div>
  </div>

  <div class="footer">
    <p class="footer-text">© 2023 Wistify. All rights reserved.</p>
  </div>
</template>

<script>

import NavBar from "./NavBar.vue";

export default {
  components: {NavBar},
  data() {
    return {
      popularOptions: ['Math', 'English', 'Physics', 'Chemistry', 'Biology']
    }
  },
  methods: {
    getButtonWidth(option) {
      return `popular-option-${option.length > 6 ? 'long' : 'short'}`;
    }
  }
}
</script>

<style scoped>
/* Import Montserrat font from Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Gochi+Hand&family=Montserrat:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');

/* Remaining styles */

.hero-section {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  background-image: url("public/Background.svg");
  background-repeat: no-repeat;
  background-size: cover;
  display: flex;
  justify-content: space-between; /* Ensure menu is at the end */
  align-items: center; /* Center items vertically */
  width: 100%; /* Adjusted to full width */
  height: 50rem; /* Converted to rem - Adjusted to a suitable height for desktop */
  flex-shrink: 0;
}

.hero-content {
  margin-bottom: 8rem;
}

.hero-section-heading {
  color: #FCFBFC;
  font-family: 'Montserrat', sans-serif;
  text-align: left;
  text-shadow: 0px 4px 15px rgba(0, 0, 0, 0.60);
  font-weight: 600;
  font-size: 3rem;
  margin-bottom: 2rem;
  line-height: normal;
  margin-left: 14.6rem; /* Adjusted space from the left edge in rem */
}

.highlight-font {
  font-family: 'Gochi Hand', cursive;
  font-size: 4rem;
}

.search-container {
  margin-top: 1rem;
}

.search-bar-container {
  display: flex;
  align-items: center;
}

.search-bar {
  font-family: 'Montserrat', sans-serif;
  width: 52.6875rem;
  height: 2.5rem;
  background-color: #FFF;
  box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.60);
  border-radius: 0.469rem 0  0 0.469rem ;
  padding: 0.5rem 1rem;
  border: none;
  font-size: 1rem;
  color: rgba(0, 0, 0, 0.4);
  margin-left: 14.6rem; /* Adjusted space from the left edge in rem */
}

.search-button {
  background-image: url('public/SearchIcon.svg'); /* Insert the correct path to your image */
  background-repeat: no-repeat;
  background-position: center;
  width: 4.6875rem; /* Converted width to rem */
  height: 2.5rem;
  background-color: #B8E830;
  color: #FFF;
  border: none;
  border-radius: 0 0.469rem 0.469rem 0;
  font-size: 1rem;

  padding: 0.5rem 1rem;
}

.search-button:hover {
  cursor: pointer;
  background-color: #8CB024;
}

.search-button:hover {
  cursor: pointer;
}

.popular-options {
  display: flex;
  align-items: center;
  margin-top: 1rem;
  font-family: 'Montserrat', sans-serif;
  font-size: 1rem;
  margin-left: 14.6rem; /* Adjusted space from the left edge in rem */
  color: #FCFBFC;
}

.popular-label {
  margin-right: 0.5rem;
  font-weight: 600;
  color: #FCFBFC;
}

.popular-option-long {
  margin-right: 0.5rem;
  font-weight: 600;
  cursor: pointer;
  min-width: 6rem; /* Adjust the minimum width for longer text */
  height: 2rem;
  border: 1px solid #FCFBFC;
  border-radius: 0.625rem;
  background: transparent;
  color: #FCFBFC;
  display: flex;
  align-items: center;
  justify-content: center;
}

.popular-option-short {
  margin-right: 0.5rem;
  font-weight: 600;
  cursor: pointer;
  min-width: 4rem; /* Adjust the minimum width for shorter text */
  height: 2rem;
  border: 1px solid #FCFBFC;
  border-radius: 0.625rem;
  background: transparent;
  color: #FCFBFC;
  display: flex;
  align-items: center;
  justify-content: center;
}

.popular-option-long:hover,
.popular-option-short:hover {
  background-color: #FCFBFC;
  color: #000;
  cursor: pointer;
}

/* Footer styles */
.footer {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  width: 100%;
  height: 8.5rem;
  background-color: #E3F3B6;
}

.footer-text {
  color: #000000; /* Text color */
  margin-top: 4rem;
  text-align: center;
  font-family: 'Montserrat', sans-serif;
  font-size: 0.8rem; /* Adjust the font size */
}

</style>