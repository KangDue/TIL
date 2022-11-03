<template>
  <div id="app">
    <h1>SSAFY TUBE</h1>
    <iframe
      :width="width"
      :height="height"
      :src="`https://www.youtube.com/embed/${videoId}`"
      title="YouTube video player"
      frameborder="0"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
      allowfullscreen
    ></iframe>
  </div>
</template>

<script>
// my youtube api key: AIzaSyDvJejVFY-wCtazPPaTpEkcoKhoabfocDI
import axios from 'axios'
export default {
  name: 'App',
  data() {
    return {
      videoId:"jAH3MEsh3aU",
      width:"640",
      height:"480",
    }
  },
  methods:{

  },
  created() {
    console.log("생성됨.",process.env)
    axios({
      method:'GET',
      params:{
        key:process.env.YOUTUBE_KEY,
        part:'snippet',
        q:'pokemon',
        maxResults: 5,
        type: 'video',
        videoDuration: 'long'
      },
      url:'https://www.googleapis.com/youtube/v3/search?',
    })
    .then((response) => console.log(response.data))

  }

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
