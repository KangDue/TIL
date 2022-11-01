const app = Vue.createApp({
    data() {
        return {
            cart:[],
            premium:1,
        }
    },
    methods:{
        updateCart(id) {
            this.cart.push(id)
        }
    },
})