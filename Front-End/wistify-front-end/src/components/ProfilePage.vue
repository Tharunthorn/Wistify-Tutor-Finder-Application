<template>
  <div>
    <Navbar />
    <div class="page-background"></div>
    <div class="square-layout">
      <div class="container">
        <div class="avatar-upload">
          <div class="avatar-edit">
            <input type="file" id="imageUpload" accept=".png, .jpg, .jpeg" @change="readURL" />
            <label for="imageUpload"></label>
          </div>
          <div class="avatar-preview">
            <div :style="{ 'background-image': 'url(' + imageSrc + ')' }"></div>
          </div>
        </div>
      </div>
    </div>
    <div class="footer">
      <p class="footer-text">© 2023 Wistify. All rights reserved.</p>
    </div>
  </div>
</template>

<script>
import Navbar from './NavBar.vue';

export default {
  components: {
    Navbar,
  },
  data() {
    return {
      imageSrc: '/public/Default_pfp.svg',
    };
  },
  methods: {
    readURL(event) {
      const input = event.target;
      if (input.files && input.files[0]) {
        const reader = new FileReader();
        reader.onload = (e) => {
          this.imageSrc = e.target.result;
        };
        reader.readAsDataURL(input.files[0]);
      }
    },
  },
};
</script>

<style scoped>
/* Import fonts as needed */

.page-background {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  background-color: #F6F6F6;
  background-repeat: no-repeat;
  background-size: cover;
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  height: 50rem;
  flex-shrink: 0;
}

.square-layout {
  position: fixed;
  top: 15%;
  left: 3.5%;
  width: 1400px;
  height: 350px;
  flex-shrink: 0;
  border-radius: 40px;
  background: #0D0C0C;
  align-items: center;
  /* Add additional styling for the square layout as needed */
}

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

body {
  background: whitesmoke;
  font-family: 'Open Sans', sans-serif;
}
.container {
  max-width: 960px;
  width: 430px;
}
h1 {
  font-size: 20px;
  text-align: center;
  margin: 20px 0 20px;
}
h1 small {
  display: block;
  font-size: 15px;
  padding-top: 8px;
  color: gray;
}
.avatar-upload {
  position: relative;
  max-width: 205px;
  margin: 45px auto;
}
.avatar-upload .avatar-edit {
  position: absolute;
  right: -20px;
  z-index: 1;
  top: 10px;
}
.avatar-upload .avatar-edit input {
  display: none;
}
.avatar-upload .avatar-edit input + label {
  display: inline-block;
  width: 34px;
  height: 34px;
  margin-bottom: 0;
  border-radius: 100%;
  background: #FFFFFF;
  border: 1px solid transparent;
  box-shadow: 0px 2px 4px 0px rgba(0, 0, 0, 0.12);
  cursor: pointer;
  font-weight: normal;
  transition: all 0.2s ease-in-out;
}
.avatar-upload .avatar-edit input + label:hover {
  background: #f1f1f1;
  border-color: #d6d6d6;
}
.avatar-upload .avatar-edit input + label:after {
  content: "\f040";
  font-family: 'FontAwesome';
  color: #757575;
  position: absolute;
  top: 10px;
  left: 0;
  right: 0;
  text-align: center;
  margin: auto;
}
.avatar-upload .avatar-preview {
  width: 250px;
  height: 250px;
  position: relative;
  border-radius: 100%;
  border: 6px solid #F8F8F8;
  box-shadow: 0px 2px 4px 0px rgba(0, 0, 0, 0.1);
}
.avatar-upload .avatar-preview > div {
  width: 100%;
  height: 100%;
  border-radius: 100%;
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
}

/* Add more styles as needed for different profile sections */
</style>
