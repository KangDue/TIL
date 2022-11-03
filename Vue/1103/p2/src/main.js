import Vue from 'vue'
import App from './App.vue'
// import AppSec from './AppSec.vue'

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')