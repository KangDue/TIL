<template>
  <div class="menu-list">
    <h1> 1. 음료를 고르세요.</h1>
    <MenuListItem v-for="(menu,idx) in menuList"
     :key="idx" 
     :menu="menu"/>
  </div>
</template>

<script>
import MenuListItem from '@/components/MenuListItem'
export default {
  name: 'MenuList',
  components: {
    MenuListItem
  },
  computed: {
    menuList: function () {
      return this.$store.state.menuList
    },
  },
  methods: {
    selectMenu: function () {},
  },
}
</script>

<style>
.menu-list{
  margin:10px;
  background: white;
  border-radius: 10px;
}
</style>