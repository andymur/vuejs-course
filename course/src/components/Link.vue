<template>
    <div>
        <div>
            Here we have a Link: {{ url }}
        </div>
        <div>Category: {{ category }}</div>
        <div> Tags:
            <div v-for="tag in tags" v-bind:key="tag">
                #{{ tag }}
            </div>
        </div>
    </div>
</template>

<script>
export default {
  props: {
      url: {
          type: String
      },
      category: {
        type: String
      },
      tags: {
        type: Array,
        default: function() {
          return []
        }
      }
  },
  data: function() {
    return {}
  },
  mounted() {
  }
};
</script>
