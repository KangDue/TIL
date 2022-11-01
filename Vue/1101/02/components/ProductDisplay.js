app.component('product-display', {
    props:{
        premium:{
            type:Number,
            required:true, // prop validation
        }
    },
    template:
    /*html*/
    `<div class="product-display">
    <div class="product-container">
      <div class="product-image">
        <img v-bind:src="image">
      </div>
      <div class="product-info">
        <h1>{{ title }}</h1>
        <p v-if="TrueOrFalse()">In Stock</p>
        <p v-else>Out of Stock</p>

        <p>Shipping: {{ shipping }}</p>
        <ul>
          <li v-for="detail in details">{{ detail }}</li>
        </ul>
        <div
         v-for="(variant,index) in variants" 
         :key="variant.id" 
         @mouseover="updateVariant(index)" 
         class="color-circle" 
         :style="{backgroundColor:variant.color}">
        </div>
        <button 
        class="button" 
        :class="{'disabledButton':!inStock,'cat':1}" 
        v-on:click="addToCart" 
        :disabled="!inStock"> 
        Add to Cart
        </button>
      </div>
    </div>
  </div>`,
  data() {
    return {
        product:'boot',
        selectedVariant:0,
        details:['50% cotton','30% wool','20% polyester'],
        variants:[
            {id:2234,color:'green',image:'./assets/images/socks_green.jpg',quantity:50},
            {id:2235,color:'blue',image:'./assets/images/socks_blue.jpg',quantity:0},
        ],
        brand: 'Vue Mastery',
        }
    },
    methods:{
            TrueOrFalse() {
                return 1
            
            },
            addToCart() {
                this.$emit('add-to-cart',this.variants[this.selectedVariant].id)
                this.cart += 1
                this.variants[this.selectedVariant].quantity -= 1
            },
            updateVariant(e) {
                this.selectedVariant = index
            }
    },
    computed: {
        title() {
            return this.brand + ' ' + this.product
        },
        image() {
            return this.variants[this.selectedVariant].image
        },
        inStock() {
            return this.variants[this.selectedVariant].quantity
        },
        shipping() {
            if (this.premium) {
                return 'Free'
            }
            return 2.99
        }
    }
})