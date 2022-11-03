<template>
  <div id="Timetable">
    <h2>예약 페이지</h2>
    <h3>선생님 선택</h3>
    <!-- 마우스 올려도 색변경, 때면 복귀, 확정시 확정 변경 -->
    <!-- 클릭시 선생님 이름 저장 -->
    <div class="teacher-grid">
      <div></div><div></div>
      <div class="normalBox" @click="teacherSelect('한상현',0)" :class="{selected:teacherSelected[0]}">한상현</div>
      <div class="normalBox" @click="teacherSelect('장미림',1)" :class="{selected:teacherSelected[1]}">장미림</div>
    </div>
    <hr>
    <!-- 9시부터 17:30까지 30분 단위--> 
    <!-- 버튼 클릭시 해당 시간 정보 배열로, 버튼 클릭시 배경 색상 변경 -->
    <h3>시간 선택</h3>
    <div>
      <div class="time-grid">
        <div style="color:#424242;" 
        v-for="(time,index) in times"
        :key="index" @click="timeSelect(index)" 
        :class="{selected:timeSelected[index]}" >{{ time }}</div>
      </div>
    </div>
    <div class="normalBox" 
    style="margin-top:50px; width:200px; margin-left:auto; margin-right:auto" @click="sendInfo">
    예약 확정</div>

  </div>

</template>

<script>
import _ from 'lodash'

export default {
  name:'TimeTable',
  data() {
    return {
      times: [
        "09:00","09:30","10:00","10:30","11:00","11:30",
        "12:00","12:30","13:00","13:30","14:00","14:30",
        "15:00","15:30","16:00","16:30","17:00","17:30",
      ],
      timeSelected:_.range(0,30,1).fill(false),
      time_count:0,
      react:0,

      teacherSelected:[false,false],
      teacherName:'',
    }
  },
  computed:{
    check() {
      this.react
      return this.times.filter((val,key) => {
        if (this.timeSelected[key]===true) {
          return true
        }
      }).join(',')
    },
  },
  methods:{
      timeSelect(index) {
        if (this.time_count === 5) {
          if (this.timeSelected[index]===true) {
            this.timeSelected[index] = !this.timeSelected[index]
            this.time_count -= 1
            this.$forceUpdate()
            return 0
          }
          alert('5타임까지만 신청할 수 있습니다.')
          return 0

        }
        if (this.timeSelected[index]===true) { 
          console.log(1)
          this.time_count -= 1
            }
        else {this.time_count+=1}
        this.timeSelected[index] = !this.timeSelected[index]
        this.$forceUpdate()
        return 0
      },

      teacherSelect(teacher,index) {
        if (this.teacherSelected[index]) {
          this.teacherName = ''
        }
        else {
          this.teacherName = teacher
          this.teacherSelected[!index+0] = false
          console.log(!index+0)
        }
        this.teacherSelected[index] = !this.teacherSelected[index]
        this.$forceUpdate()
      },

      sendInfo() {
        
        if (this.time_count===0 && this.teacherName==''){
          alert('선생님과 상담 시간 모두 골라주세요.')
        }
        else if (this.teacherName==='') {
          alert('선생님을 골라주세요.')
        }
        else if (this.time_count===0) {
          alert('상담시간을 골라주세요.')
        }
        else { 
          alert('신청합니다.')
          this.react++
          this.$emit('data-submit',this.teacherName, this.check)
          this.timeSelected = _.range(0,30,1).fill(false)
          this.time_count = 0
          this.react = 0
          this.teacherSelected = [false,false]
          this.teacherName = ''
        }
      },
    },
}
</script>

<style>
.normalBox {
  border: 1px solid black;
}

.teacher-grid {
  display:grid;
  grid-template-columns: repeat(6,1fr);
  gap:10px;
}

.time-grid {
  display:grid;
  grid-template-columns: repeat(6,1fr);
}

.selected {
  color: #0F4181;
  background: #658dc63d;
}
</style>