<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <div>Hi There!</div>
    <customlink />
  </div>
</template>

<script>
// @ is an alias to /src
import Link from "@/components/Link.vue";
import axios from "axios";

export default {
  name: "linksview",
  components: {
    "customlink": Link
  },
  methods: {
  },
  data: function() {
    return {
      links: []
    };
  }
};
</script>
