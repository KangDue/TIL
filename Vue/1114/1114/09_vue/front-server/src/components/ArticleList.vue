<template>
  <div class="article-list">
    <hr>
    <h3>Article List</h3>
    <hr>
    <div v-if="articles">
      <ArticleListItem v-for="(article,idx) in articles" 
      :key="idx" 
      :article="article"/>
    </div>

  </div>
</template>

<script>
import ArticleListItem from '@/components/ArticleListItem.vue'

export default {
  name: 'ArticleList',
  components: {
    ArticleListItem
  },
  data(){
    return {
    }
  },
  computed: {
    articles() {
      return this.$store.state.articles
    }
  },
  methods:{
  }
}

</script>

<style>
.article-list {
  text-align: start;
  
}
</style>
