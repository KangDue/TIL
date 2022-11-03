<template>
  <div id="app">
    <h1 style="color:rgb(10,150,255);">SSAFY TUBE</h1>
    <iframe
      :width="width"
      :height="height"
      :src="`https://www.youtube.com/embed/${videoId}`"
      title="YouTube video player"
      frameborder="0"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
      allowfullscreen
    ></iframe>
    <div style="border:1px dased gray;"><h1>{{ title }}</h1></div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'App',
  data() {
    return {
      videoId:"",
      width:"640",
      height:"480",
      title:"",
    }
  },
  methods:{
  },
  created() {
    console.log("생성됨.",process.env)
    axios({
      method:'GET',
      params:{
        key:process.env.VUE_APP_YOUTUBE_API_KEY,
        q:'코딩노래',
        type: 'video',
        part: 'snippet',
      },
      url:'https://www.googleapis.com/youtube/v3/search?',
    })
    .then((response) => {
      this.videoId=response.data.items[0].id.videoId
      this.title=response.data.items[0].snippet.title
    })
    .catch(() => {
      console.log("초기 요청 실패")
      })
  },

}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
