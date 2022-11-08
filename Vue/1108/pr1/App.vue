<template>
  <div>
    <h1 v-for="(val,idx) in calls" :key="idx"> {{val.id}} </h1>
  </div>
</template>

<script>
export default {
  name:'App',
  methods:{},
  computed:{
    calls() {
      return this.$store.state.list
    }
  },

}
</script>

<style>

</style>