<template>
  <div class="hello" @click="select" :class="{selected:selected}">
    {{ time }}
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    time: String,
    idx:Number,
  },
  data() {
    return {
      selected:false,
    }
  },
  methods:{
    select() {
      this.selected = !this.selected
      this.$emit('append',this.time,this.idx)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.hello {
  padding: 12px;

}

.selected {
  color: #0F4C81;
  background: #658dc63d;
}
</style>
