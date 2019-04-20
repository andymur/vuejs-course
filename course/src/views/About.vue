<template>
  <div class="about">
    <h1>This is an about page</h1>
    <UserForm></UserForm>
  </div>
</template>

<script>
// @ is an alias to /src
import UserForm from "@/components/UserForm.vue";

export default {
  name: "about",
  components: {
    UserForm
  }
};
</script>
