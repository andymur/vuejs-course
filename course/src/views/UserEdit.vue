<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <div v-if="!userData"></div>
    <user-form
      v-else
      :userdata="userData"
      @userChanged="userChanged"
    ></user-form>
    <button type="button" id="submit" @click="editUser(userId)">Edit</button>
    <pre> {{ userData }} </pre>
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
  methods: {
    loadUser: function(userId) {
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
    editUser: function(userId) {
      var self = this;
      axios
        .patch("http://localhost:5000/useredit/" + userId, this.userData, {
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
  computed: {
    userId: function() {
      return this.$route.params.id;
    }
  },
  created: function() {
    this.loadUser(this.userId);
  },
  data: function() {
    return {
      userData: null
    };
  }
};
</script>
