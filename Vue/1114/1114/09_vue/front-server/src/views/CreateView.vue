<!-- views/CreateView.vue -->

<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model.trim="title"><br>
      <label for="content">내용 : </label>
      <textarea id="content" cols="30" rows="10" v-model="content"></textarea><br>
      <input type="submit" id="submit">
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'CreateView',
  data() {
    return {
      title:null,
      content:null
    }
  },
  methods: {
    createArticle() {
      let article = {
        title:this.title,
        content:this.content
      }
      if (!this.title) {
        alert("제목을 입력해 주세요")
        return 0
      }
      else if(!this.content) {
        alert("내용을 입력해 주세요")
        return 0
      }
      axios.post('http://127.0.0.1:8000/api/v1/articles/'
      ,article,{headers:{
          Authorization: `Token ${this.$store.state.token}`
        }}) // data는 obj 그대로 넣자.
      .then(res => {
        console.log(res.data)
        // this.$store.dispatch('createArticle',res.data) 별도의 직접적인 추가 x
        this.$router.push({name:'ArticleView'}) // 홈으로 보내서 data 갱신
      })
      .catch(console.log)
    }
  }
}
</script>

<style>

</style>
