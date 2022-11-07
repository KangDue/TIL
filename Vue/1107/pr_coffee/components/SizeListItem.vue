<template>
  <div>
    <div class='plate' @click="selectSize" :class="{selected:size.selected}">
      <div class="inner">{{ size.name }}</div>
      <div class="inner">{{ size.price }}원</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SizeListItem',
  props: {
    size: Object,
  },
  methods:{
    selectSize() {
      this.$store.dispatch('selectSize',this.size)
    }
  }
}
</script>

<style>
.plate{
  display:flex;
  flex-direction:row;
  justify-content: space-between;
  align-items: center;
  border-radius: 10px;
  border:2px solid black;
  height:60px;
  cursor: pointer;
}

.inner {
  margin-right:10px;
  margin-left:10px;
}

.selected{
  background: rgb(0,150,20);
  color:white;
}
</style>