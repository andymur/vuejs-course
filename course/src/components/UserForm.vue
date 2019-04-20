<template>
  <form id="user-form">
    <div>
      <span>First Name</span>
      <div>
        <input type="text" size="50" v-bind:value="userdata.firstName" />
      </div>
    </div>
    <div>
      <span>Last Name</span>
      <div>
        <input type="text" size="50" v-bind:value="userdata.secondName" />
      </div>
    </div>
    <div>
      <span>Patronymic</span>
      <div>
        <input type="text" size="50" v-bind:value="userdata.patronymic" />
      </div>
    </div>
    <button type="button" id="submit" v-if="editForm">Edit</button>
    <button type="button" id="submit" v-else>Add</button>
  </form>
</template>

<script>
export default {
  data: function() {
    return {};
  },
  props: {
    userdata: {
      type: Object,
      default: function() {
        return {};
      }
    },
    editForm: Boolean
  }
};
</script>
