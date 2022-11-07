<template>
  <div>
    <div class='plate' @click="selectMenu" :class="{selected:menu.selected}">
      <img class="inner" :src="menu.image" alt="" style="height:40px; width:40px; display:box;">
      <div class="inner">{{ menu.title }}</div>
      <div class="inner">{{ menu.price }}원</div>
    </div>

  </div>
</template>

<script>
export default {
  name: 'MenuListItem',
  props: {
    menu: Object,
  },
  methods:{
    selectMenu() {
      this.$store.dispatch('selectMenu',this.menu)
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
}

.inner {
  margin-right:10px;
  margin-left:10px;
}

.selected{
  background: rgb(0,150,20);
  color: white;
}
</style>