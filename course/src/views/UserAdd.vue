<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <user-form :userdata="userData"></user-form>
    <button type="button" id="submit">Add</button>
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
  },
  data: function() {
    return {
      userData: {}
    };
  }
};
</script>
