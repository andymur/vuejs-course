<style type="text/css">
div#grid {
  margin-top: 1vw;
  width: 60%;
  display: grid;
  grid-template-columns: 30px 1fr 1fr 1fr 20px;
  grid-auto-rows: 50px;
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
    <span v-show="show">Number of users: {{ userCount }}</span>
    <div id="grid" v-show="show">
      <div class="gridheader">ID</div>
      <div class="gridheader">NAME</div>
      <div class="gridheader">SURNAME</div>
      <div class="gridheader">PATRONYMIC</div>
      <div class="gridheader">AVATAR</div>
      <div v-for="item in users" v-bind:key="item.id">
        <div class="gridcell" v-bind:id="'uid' + item.id + '_id'">
          <router-link :to="{ name: 'user-edit', params: { id: item.id } }">
            {{ item.id }}
          </router-link>
        </div>
        <div class="gridcell" v-bind:id="'uid' + item.id + 'firstname'">
          {{ item.firstName }}
        </div>
        <div class="gridcell" v-bind:id="'uid' + item.id + '_secondname'">
          {{ item.secondName | capitalize }}
        </div>
        <div class="gridcell" v-bind:id="'uid' + item.id + '_patronymic'">
          {{ item.patronymic }}
        </div>
        <div class="gridcell" v-bind:id="'uid' + item.id + '_avatar'">
          <img
            source
            v-bind:src="getAvatarLink(item)"
            height="30px"
            type="img"
          />
        </div>
      </div>
    </div>
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
    },
    show: {
      type: Boolean,
      default: true
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
