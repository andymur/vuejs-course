<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <!-- HelloWorld msg="Welcome to Your Vue.js App" / -->
    <users-list :users="gridData"></users-list>
  </div>
</template>

<script>
// @ is an alias to /src
import UsersList from "@/components/UsersList.vue";
import axios from "axios";

export default {
  name: "about",
  components: {
    "users-list": UsersList
  },
  mounted: function() {
    console.log("App has been mounted!");
    var self = this;
    axios
      .get("http://localhost:5000/users/")
      .then(response => (this.gridData = response.data))
      .catch(function(error) {
        self.gridData = [];
        console.error("cannot read user list from API " + error);
      });
  },
  data: function() {
    return {
      gridData: []
    };
  }
};
</script>
