<template>
  <div>
    <h1>Detail</h1>
    <p>글 번호 : {{ article?.id }}</p>
    <p>제목 : {{ article?.title }}</p>
    <p>내용 : {{ article?.content }}</p>
    <p>작성시간 : {{ createdAt }}</p>
    <p>수정시간 : {{ updatedAt }}</p>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'DetailView',
  data() {
    return {
      article:null,
      createdAt:null,
      updatedAt:null
    }
  },
  created() {
    console.log(this.article)
    this.getArticleDetail()
  },
  methods: {
    getArticleDetail() {
      axios.get(`http://127.0.0.1:8000/api/v1/articles/${this.$route.params.id}/`)
      .then((res)=>{
        console.log(res)
        this.createdAt = new Date(res.data.created_at).toLocaleString()
        this.updatedAt = new Date(res.data.updated_at).toLocaleString()
        this.article=res.data
      })
      .catch(console.log)
    }
  }
}
</script>
