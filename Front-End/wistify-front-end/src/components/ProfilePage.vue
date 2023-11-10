<template>
  <div>
    <Navbar />
    <div class="page-background"></div>
    <div class="square-layout">
      <div class="profile-pic">
        <label class="-label" for="file">
          <span class="glyphicon glyphicon-camera"></span>
          <span>Change Image</span>
        </label>
        <input id="file" type="file" @change="loadFile" />
        <img v-if="imageSrc" :src="imageSrc" id="output" width="200" height="200" />
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
      imageSrc: 'https://upload.wikimedia.org/wikipedia/commons/2/2c/Default_pfp.svg',
    };
  },
  methods: {
    loadFile(event) {
      this.imageSrc = URL.createObjectURL(event.target.files[0]);
    },
  },
};
</script>

<style scoped>
/* Import Montserrat font from Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');

.page-background {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  background-image: url("public/Background.svg");
  opacity: 0.3;
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
  background: green;
  align-items: center;
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
  color: #000000;
  margin-top: 4rem;
  text-align: center;
  font-family: 'Montserrat', sans-serif;
  font-size: 0.8rem;
}

.profile-pic {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;

  input {
    display: none;
  }

  img {
    position: absolute;
    object-fit: cover;
    width: 165px;
    height: 165px;
    box-shadow: 0 0 10px 0 rgba(255, 255, 255, .35);
    border-radius: 100px;
    z-index: 0;
  }

  .-label {
    cursor: pointer;
    height: 165px;
    width: 165px;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: rgba(0, 0, 0, 0.8);
    color: rgb(250, 250, 250);
    border-radius: 100px;
    opacity: 0; /* Initially hide the label */
    transition: opacity 0.2s ease-in-out;
  }

  &:hover .-label {
    opacity: 1; /* Show the label on hover */
  }

  span {
    display: inline-flex;
    padding: 0.2em;
    height: 2em;
  }
}
</style>
