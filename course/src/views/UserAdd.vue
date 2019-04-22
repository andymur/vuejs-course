<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <user-form :userdata="userData" @userChanged="userChanged"></user-form>
    <button type="button" id="submit" @click="addUser">Add</button>
    <pre> {{ userData }} </pre>
  </div>
</template>

<script>
// @ is an alias to /src
import UserForm from "@/components/UserForm.vue";
import axios from "axios";

var emptyUser = {
  id: 0,
  firstName: "",
  secondName: "",
  patronymic: "",
  avatarLink: null
};

export default {
  name: "useradd",
  components: {
    "user-form": UserForm
  },
  methods: {
    addUser: function() {
      var self = this;
      axios
        .patch("http://localhost:5000/useredit/0", this.userData, {
          headers: { "Content-Type": "application/json" }
        })
        .then(function(response) {
          self.userData = Object.assign({}, response.data);
        })
        .catch(function(error) {
          self.userData = {};
          console.error("cannot read user list from API " + error);
        });
      this.$router.push("/");
    },
    userChanged: function(newUserData) {
      console.log("User has been changed: " + newUserData.patronymic);
      this.userData = Object.assign({}, newUserData);
    }
  },
  data: function() {
    return {
      userData: emptyUser
    };
  }
};
</script>
