<template>
    <div>
        <div>
            Here we have a Link: {{ link.url }}
        </div>
        <div>Category: {{ link.category }}</div>
        <div> Tags:
            <div v-for="tag in link.tags" v-bind:key="tag">
                #{{ tag }}
            </div>
        </div>
    </div>
</template>

<script>
export default {
  props: {
      linkdata: {
          type: Object,
          default: function() {
              return {"id": 2, "url": "http://javascript.ru", "category": "Applied", "tags": ["js"]}
          }
      }
  },
  data: function() {
    return {
      link: {}
    };
  },
  mounted() {
    this.link = Object.assign({}, this.linkdata);
  }
};
</script>
