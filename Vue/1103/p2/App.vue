<template>
  <div id="app">
    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    <h2>예약 페이지</h2>
    <h3>선생님 선택</h3>
    <div class="tgd">
      <TeacherName v-for="(tname,index) in teachers" :key="index" :tname="tname" :idx="index" @append="append"></TeacherName>
    </div>
    <hr>
    <h3>시간 선택</h3>
    <div class="gd">
      <HelloWorld v-for="(time,index) in times" :key="index" :time="time" :idx="index" @append="append"/>
    </div>
    <hr>
    <h1>선택 시간 : {{ checked }}</h1>
  </div>
</template>

<script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>
<script>
import TeacherName from './components/TeacherName.vue'
import HelloWorld from './components/HelloWorld.vue'
import _ from 'lodash'
export default {
  name: 'App',
  data() {
    return {
      teachers:['','','Eric','Tony','',''],
      times: [
        "09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30",
        "14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30",
        "19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30",
      ],
      selected:_.range(0,30,1).fill(0),
      i:0,
      count:0,
    }
  },
  methods:{
    append(x,y) {
      this.count = 0
      this.selected.forEach((val) => {this.count+=val})
      if (this.count===5){
        alert('5타임 까지만 신청할 수 있습니다.')
        return 0
      }

      this.selected[y] = this.selected[y] ? 0:1
      this.i++
    }
  },
  computed:{
    checked() {
      this.i
      return this.times.filter((val,key) => {
        console.log(val,key)
        if (this.selected[key] > 0) {
          return true
        }
      }).join(' ')
    }
  },
  components: {
    HelloWorld,
    TeacherName,
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
  width:450px;
}
.gd{
  display: grid;
  grid:'. . . . . . . .';
  gap: 5px;
  /* border: 16px solid silver; */

}

.tgd{
  display: grid;
  grid:'. . . . . .';
  gap: 10px;
  /* border: 16px solid silver; */

}
</style>
