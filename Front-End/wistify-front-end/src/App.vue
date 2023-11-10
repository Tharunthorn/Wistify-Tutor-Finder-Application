<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
import ProfilePage from "./components/ProfilePage.vue";

export default {
  components: {ProfilePage}
  // Your logic for the App component
};
</script>
