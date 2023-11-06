<template>
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
      </div>
    </div>
  </div>
</template>


<script>
export default {
  // You can add component logic here if needed
}
</script>

<style scoped>
/* Import Montserrat font from Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Gochi+Hand&family=Montserrat:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');

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
  border-radius: 0.469rem;
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
  height: 3.5rem;
  background-color: #B8E830;
  color: #FFF;
  border: none;
  border-radius: 0 0.469rem 0.469rem 0;
  font-size: 1rem;
  margin-left: -4.69rem;
  padding: 0.5rem 1rem;
}

.search-button:hover {
  cursor: pointer;
  background-color: #8CB024;
}

.search-button:hover {
  cursor: pointer;
}
</style>
