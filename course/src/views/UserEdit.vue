<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <!-- HelloWorld msg="Welcome to Your Vue.js App" / -->
    <user-form :userdata="userData" :editForm="true"></user-form>
  </div>
</template>

<script>
// @ is an alias to /src
import UserForm from "@/components/UserForm.vue";
import axios from "axios";

export default {
  name: "useredit",
  components: {
    "user-form": UserForm
  },
  mounted: function() {
    var userId = this.$route.params.id;
    console.log("App has been mounted, and id is " + userId);
    var self = this;
    axios
      .get("http://localhost:5000/user/" + userId)
      .then(response => (this.userData = response.data))
      .catch(function(error) {
        self.userData = {};
        console.error("cannot read user list from API " + error);
      });
  },
  data: function() {
    return {
      userData: {}
    };
  }
};
</script>
