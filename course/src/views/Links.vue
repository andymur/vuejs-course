<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <div>Hi There!</div>
    <customlink
      url="javascript.ru"
      category="Applied"
      v-bind:tags="['js', 'magic']"
    />
  </div>
</template>

<script>
// @ is an alias to /src
import Link from "@/components/Link.vue";

export default {
  name: "linksview",
  components: {
    customlink: Link
  },
  methods: {},
  data: function() {
    return {
      links: []
    };
  }
};
</script>
