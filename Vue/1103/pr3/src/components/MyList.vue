<template>
  <div id="#MyList">
    <h2>상담 신청 현황</h2>
    <h3>상담 성생님</h3>
    <p> 성함 : {{ teacherName }}</p>
    <hr>
    <h3>예약 현황</h3>
    <p>시간들 : {{ timeList }}</p>
    <hr>
    <img src="@/assets/ssafy-logo.png" style="margin-top:50px;">
  </div>
</template>

<script>
export default {
  name:'MyList',
  props:{
    teacherName:String,
    timeList:String,
  }
}
</script>

<style>

</style>