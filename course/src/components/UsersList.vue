<style type="text/css">
div#grid {
  margin-top: 1vw;
  width: 60%;
  display: grid;
  grid-template-columns: 30px 1fr 1fr 1fr 20px;
  grid-auto-rows: 50px;
}

table#grid {
  width: 60%;
}

div.gridcell {
  font-size: 12pt;
}
div.gridheader {
  font-weight: bold;
}
</style>

<template id="user-list">
  <div>
    <span>Number of users: {{ userCount }}</span>
    <table id="grid" >
      <tr>
        <th class="gridheader">ID</th>
        <th class="gridheader">NAME</th>
        <th class="gridheader">SURNAME</th>
        <th class="gridheader">PATRONYMIC</th>
        <th class="gridheader">AVATAR</th>
      </tr>
      <tr v-for="item in users" v-bind:key="item.id">
        <td class="gridcell" v-bind:id="'uid' + item.id + '_id'">
          <router-link :to="{ name: 'user-edit', params: { id: item.id } }">
            {{ item.id }}
          </router-link>
        </td>
        <td class="gridcell" v-bind:id="'uid' + item.id + 'firstname'">
          {{ item.firstName }}
        </td>
        <td class="gridcell" v-bind:id="'uid' + item.id + '_secondname'">
          {{ item.secondName | capitalize }}
        </td>
        <td class="gridcell" v-bind:id="'uid' + item.id + '_patronymic'">
          {{ item.patronymic }}
        </td>
        <td class="gridcell" v-bind:id="'uid' + item.id + '_avatar'">
          <img
            source
            v-bind:src="getAvatarLink(item)"
            height="30px"
            type="img"
          />
        </td>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  data: function() {
    return {};
  },
  props: {
    users: {
      type: Array,
      default: function() {
        return [];
      }
    }
  },
  methods: {
    getAvatarLink: function(item) {
      return item.avatarLink == null
        ? "http://s3.amazonaws.com/37assets/svn/765-default-avatar.png"
        : item.avatarLink;
    }
  },
  filters: {
    capitalize: function(value) {
      value = value.toString();
      if (!value) return "";
      return value.toUpperCase();
    }
  },
  computed: {
    userCount: function() {
      return this.users.length;
    }
  }
};
</script>
