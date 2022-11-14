<template>
  <div>
      <router-link :to="{ name:'DetailView',params:{id:article.id}}">Detail</router-link>
    <div>
      <h5>PK: {{ article.id }}</h5>
      <h5>작성자: {{article.username }} </h5>
      <p>제목: {{ article.title }}</p>
      <p>내용: {{ article.content }}</p>
    </div>
    <router-view/>
    <hr> 
  </div>
</template>

<script>
export default {
  name: 'ArticleListItem',
  props:{
    article:Object,
  }
}
</script>

<style>

</style>
