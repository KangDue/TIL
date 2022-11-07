<template>
  <div id="app">
    <h1>Coffee Order App</h1>
    <div @click="addOrder">주문받기</div>
    <div class="board">
      <MenuList/>
      <SizeList/>
    </div>
    <button class="btn" 
    @click="addOrder">장바구니 담기</button>
    <OrderList/>
  </div>
</template>

<script>
import MenuList from '@/components/MenuList'
import SizeList from '@/components/SizeList'
import OrderList from '@/components/OrderList'
export default {
  name: 'App',
  components:{
    MenuList,
    SizeList,
    OrderList,
  },
  methods:{
    addOrder(){
      this.$store.commit('addOrder')
    }
  }
}
</script>

<style>
* {
  box-sizing: border-box;
  font-family: 'Noto Sans KR', sans-serif;
  padding: 0;
  margin: 0;
}

ul {
  list-style: none;
}

.board {
  display:grid;
  grid-template-columns:1fr 1fr;
  background: gray;
}

.btn{
  background: rgb(0,150,20);
  color:white;
  width:100%;
  height:60px;
  border-radius: 10px;
  margin-top:10px;
  margin-bottom:10px;
  cursor: pointer;
}
</style>
