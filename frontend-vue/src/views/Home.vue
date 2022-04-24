<template>
  <div class="home">
    <Profile />
  </div>
</template>

<script>
import Profile from "../components/Profile.vue";
import router from "../router";

export default {
  name: "Home",
  components: {
    Profile,
    //Question,
  },
  mounted() {
    this.checkLoggedIn();
  },
  methods: {
    checkLoggedIn() {
      this.$session.start();
      if (!this.$session.has("token")) {
        router.push("/auth");
      }
    },
  },
};
</script>
