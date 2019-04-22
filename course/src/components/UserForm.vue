<template>
  <form id="user-form">
    <div>
      <span>First Name</span>
      <div>
        <input type="text" size="50" v-model="user.firstName" />
      </div>
    </div>
    <div>
      <span>Last Name</span>
      <div>
        <input type="text" size="50" v-model="user.secondName" />
      </div>
    </div>
    <div>
      <span>Patronymic</span>
      <div>
        <input type="text" size="50" v-model="user.patronymic" />
      </div>
    </div>
    <div>
      local user:
      <pre>{{ user }}</pre>
    </div>
  </form>
</template>

<script>
export default {
  name: "userform",
  props: {
    userdata: {
      type: Object
    }
  },
  data: function() {
    return {
      user: {}
    };
  },
  mounted() {
    console.log(this.userdata);
    this.user = Object.assign({}, this.userdata);
  },
  watch: {
    user: {
      deep: true,
      handler: function() {
        this.$emit("userChanged", this.user);
      }
    }
  }
};
</script>
