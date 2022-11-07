<template>
  <div>
    <div class="ols">
      <h1>주문내역</h1>
      <b>총 {{ totalOrderCount }}건: {{totalOrderPrice}}원</b>
      <ol>
        <OrderListItem 
        v-for="(order,idx) of orderList" 
        :key="idx" 
        :order="order"/>
      </ol>
    </div>

  </div>
</template>

<script>
import OrderListItem from '@/components/OrderListItem'
export default {
  name: 'OrderList',
  components:{
    OrderListItem,
  },
  computed: {
    orderList: function () { 
      return this.$store.state.orderList
    },
    totalOrderCount: function () {
      return this.$store.state.orderList.length
    },
    totalOrderPrice: function () {
      let tot = 0
      for (let i of this.orderList){
        tot += i.size.price + i.menu.price
      }
      return tot
    },
  },
}
</script>

<style>
.ols{
  background:gray;
}
</style>