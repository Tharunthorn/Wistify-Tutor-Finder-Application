<template>
  <div>
    <nav class="navbar">
      <a href="/">
        <img src="public/Logo.svg" alt="WISTIFY Logo" class="navbar-logo" />
      </a>
      <div class="navbar-menu">
        <a class="navbar-item" href="/Explore">Explore</a>
        <a class="navbar-item" href="/SignUpTutor">Become Tutor</a>
        <a class="navbar-item" href="/SignIn">Sign In</a>
        <a class="navbar-item-join" href="/SignUp">Join</a>
      </div>
    </nav>
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

/* Adding styles to change the size of the navbar and logo */
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000; /* Ensures the navbar is above other content */
  background-color: rgba(0, 0, 0, 0.80);
  display: flex;
  justify-content: space-between; /* Ensure menu is at the end */
  align-items: center; /* Center items vertically */
  width: 100%; /* Adjusted to full width */
  height: 4.6667rem; /* Converted to rem - Adjusted to a suitable height for desktop */
  flex-shrink: 0;
}

.navbar-logo {
  display: flex;
  width: 6.6667rem; /* Converted to rem - Set the width */
  height: 1.7333rem; /* Converted to rem - Set the height */
  margin-top: 0.3333rem; /* Converted to rem - Adjusted the logo position */
  flex-shrink: 0; /* Prevent shrinking */
  margin-left: 14.6rem; /* Adjusted space from the left edge in rem */
}

.navbar-menu {
  margin-right: 14.6rem; /* Adjusted space from the right edge in rem */
}

.navbar-item {
  color: #FCFBFC;
  text-decoration: none;
  margin: 0.1rem; /* Converted to rem - Adjusted margin */
  font-family: 'Montserrat', sans-serif; /* Applying Montserrat font */
  line-height: normal;
  letter-spacing: -0.02rem; /* Converted to rem - Adjusted letter-spacing */
  font-weight: 500;
}

.navbar-item-join {
  color: #B8E830;
  border: 0.1rem solid #B8E830; /* Set border properties */
  border-radius: 0.3rem; /* Apply border-radius */
  padding: 0.6667rem 1.3333rem; /* 10px top and bottom, 20px left and right in rem */
  font-family: 'Montserrat', sans-serif; /* Applying Montserrat font */
  margin: 0.1rem; /* Converted to rem - Adjusted margin */
  text-decoration: none;
  line-height: normal;
  letter-spacing: -0.02rem; /* Converted to rem - Adjusted letter-spacing */
  font-weight: 500;
}

.navbar-item-join:hover {
  color: #FCFBFC;
  background-color: #B8E830; /* Change the background color on hover */
}

.navbar-item:not(:last-child) {
  margin-right: 1.7333rem; /* 26px in rem - Adjusted space between each navbar item */
}

.navbar-item:hover {
  color: #B8E830; /* Change the text color on hover */
}

/* Add media query to adjust for smaller screens, e.g., phones */
@media (max-width: 1000px) {

  .navbar {
    height: 5rem; /* Converted to rem - Adjust height for smaller screens */
  }

  .navbar-logo {
    display: block;
    margin: 0 auto; /* Center the logo when the menu is hidden */
    width: 4.8rem; /* Converted to rem - Adjusted width for smaller screens */
    height: 1.6rem; /* Converted to rem - Adjusted height for smaller screens */
    margin-top: 0.3333rem; /* Converted to rem - Adjusted logo position for smaller screens */
  }

  .navbar-menu {
    display: none; /* Hide menu items on smaller screens */
  }
}
</style>
