<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <!-- HelloWorld msg="Welcome to Your Vue.js App" / -->
    <user-form :userdata="userData" :editForm="false"></user-form>
  </div>
</template>

<script>
// @ is an alias to /src
import UserForm from "@/components/UserForm.vue";
//import axios from "axios";

export default {
  name: "useredit",
  components: {
    "user-form": UserForm
  },
  mounted: function() {
    console.log("App has been mounted!");
    /*var self = this;
    axios
      .get("http://localhost:5000/users/")
      .then(response => (this.gridData = response.data))
      .catch(function(error) {
        self.gridData = [];
        console.error("cannot read user list from API " + error);
      });*/
  },
  data: function() {
    return {
      userData: {}
    };
  }
};
</script>
