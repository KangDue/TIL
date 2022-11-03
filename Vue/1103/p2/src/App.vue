<template>
  <div id="app">
    <div style="width:450px;">
      <h2>예약 페이지</h2>
      <h3>선생님 선택</h3>
      <div class="fx">
        <div></div><div></div>
        <div class="teacher-div" v-for="(teacher,index) in teachers" 
        :key="index" 
        @click="select_teacher(teacher,index)"
         :class="{selected:selectedTeacher[index]}">{{ teacher }}
        </div>
      </div>
      <hr>
      <h3>시간 선택</h3>
      <div class="gd">
        <div class='time-div' v-for="(time,index) in times"
         :key="index" 
         @click="select_time(index)"
         :class="{selected:selectedTime[index]}">{{ time }}
        </div>
      </div>
    </div>

    <div style="width:450px; background-color:#658dc63d;">
      <h2>상담 신청 현황</h2>
      <h3>상담 선생님</h3>
      <p>성함 : {{ teacherName }}</p>
      <hr>
      <h3>예약 현황</h3>
      <p>시간들 : {{ checked }}</p>
      <hr>
      <img src="./assets/ssafy-logo.png" style="margin-top:50px; margin-bottom:50px;">
    </div>
  </div>
</template>

<script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>
<script>
import _ from 'lodash'
export default {
  name: 'App',
  data() {
    return {
      teachers:['Eric','Tony'],
      times: [
        "09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30",
        "14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30",
        "19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30",
      ],
      selectedTeacher:[0,0],
      selectedTime:_.range(0,30,1).fill(0),
      i:0,
      teacherName:'',
      time_count:0,
    }
  },
  methods:{
    select_teacher(y,index) {
      if (this.teacherName===y) {
        this.teacherName=''
        this.selectedTeacher=[0,0]
        return 0
      }
      this.selectedTeacher=[0,0]
      this.selectedTeacher[index] = 1
      this.teacherName=y
      console.log(this.teacherName)
    },
    select_time(y) {
      if (this.time_count===5) {
        alert("5타임까지만 신청할 수 있습니다.")
        return 0
      }
      this.i++
      this.selectedTime[y] = this.selectedTime[y] ? 0:1
      if (this.selectedTime[y]) {
        this.time_count += 1
      }
      else {
        this.time_count -= 1
      }
      return 0
    }
  },
  computed:{
    checked() {
      this.i
      return this.times.filter((val,key) => {
        if (this.selectedTime[key] > 0) {
          return true
        }
      }).join(' ')
    }
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
  display: flex;
  flex-direction: row;
  justify-content: space-around;
}

.gd{
  display: grid;
  grid:'. . . . . . . .';
  /* gap: 5px; */
  /* border: 16px solid silver; */
}

.fx{
  display: grid;
  grid-template-columns: repeat(6,1fr);
  gap: 10px;
  /* justify-content: center; */
  /* border: 16px solid silver; */
}

.teacher-div{
  border: 1px solid black;
  width : 100px;
}

.selected {
  color: #0F4C81;
  background: #658dc63d;
}
</style>
