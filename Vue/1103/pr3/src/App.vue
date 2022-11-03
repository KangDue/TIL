<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <div class="app-grid">
      <TimeTable @data-submit="getData"></TimeTable>
      <MyList :teacherName="teacherName" :timeList="timeList"></MyList>
    </div>
  </div>
</template>

<script>
import TimeTable from '@/components/TimeTable'
import MyList from '@/components/MyList.vue'


export default {
  name: 'App',
  components: {
    TimeTable,
    MyList
  },
  data() {
    return {
      teacherName:'',
      timeList:'',
    }
  },
  methods: {
    getData(x,y) {
      this.teacherName=x
      this.timeList=y
    },
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@700&display=swap');
#app {
  font-family: 'Noto Sans KR', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.app-grid {
  display: grid;
  grid-template-columns: 1fr 1fr ;
}
</style>
