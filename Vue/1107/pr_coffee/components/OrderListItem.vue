<template>
  <li>
    <div class='plate'>
      <div>
        <div>
          <img class="inner" :src="order.menu.image" alt="" style="height:40px; width:40px;">
                <div style="display:grid; grid-template-row:1fr 1fr;">
          <div class="inner">{{ order.menu.title }}</div>
          <div class="inner">{{ order.size.name }}</div>
        </div>
        </div>
        
      </div>
      <div class="inner">{{ totalPrice }}원</div>
    </div>
  </li>
  
</template>

<script>
export default {
  name: 'OrderListItem',
  props: {
    order: Object,
  },
  computed: {
    totalPrice: function () { 
      return this.order.menu.price + this.order.size.price
    },
  },
}
</script>

<style>
</style>