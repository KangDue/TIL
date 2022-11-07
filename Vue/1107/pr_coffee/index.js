import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    orderList: [],
    menuList: [{
      title:"아메리카노",
      price:3000,
      selected:true,
      image:"https://source.unsplash.com/featured/?americano"
      },
      {
        title:"우유",
        price:1500,
        selected:false,
        image:"https://source.unsplash.com/featured/?milk"
        },
      {
        title:"오렌지쥬스",
        price:2500,
        selected:false,
        image:"https://source.unsplash.com/featured/?orangejuice"
        }
    ],
    sizeList: [{
      name:'small',
      price:500,
      selected:true
      },
    {
      name:'medium',
      price:0,
      selected:false
      },
    {
      name:'large',
      price:500,
      selected:false
      },
    ],
  },
  getters: {
  },
  mutations: {
    addOrder: function (state) {
      let order = {}
      for (let size of state.sizeList){
        if (size.selected){ order.size=size }
      }

      for (let menu of state.menuList){
        if (menu.selected){ order.menu=menu}
      }
      state.orderList.push(order)
      console.log(state.orderList)
    },
    updateMenuList: function (state,selectedMenu) {
      for (let val of state.menuList) {
        if (val.title===selectedMenu){
          val.selected = true
          break
        }
      }
    },
    updateSizeList: function (state,selectedSize) {
      for (let size of state.sizeList) {
        if (size.name == selectedSize){
          size.selected = true
          break
        }
      }
    },
    selectMenu(state,menu){
      for (let val of state.menuList){
        if (val.title === menu.title){
          val.selected = !val.selected
        }
        else if (val.selected) {
          val.selected = !val.selected
        }
      }
    },
    selectSize(state,size){
      for (let val of state.sizeList){
        if (val.name === size.name){
          val.selected = !val.selected
        }
        else if (val.selected) {
          val.selected = !val.selected
        }
      }
    },
  },
  actions: {
    selectMenu(context,menu){
      context.commit('selectMenu',menu)
    },
    selectSize(context,size){
      context.commit('selectSize',size)
    }
  },
  modules: {
  }
})