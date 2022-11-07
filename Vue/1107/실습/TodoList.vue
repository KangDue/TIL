<template>
  <TodoListItem v-for="(todo,index) in todos" :key="index"/>
</template>

<script>
import TodoListItem from '@/components/TodoListItem'

export default {
  name:'TodoList',
  components: {
    TodoListItem,
  },
  computed: {
    todos() {
      return this.$store.state.todos
    }
  }
}
</script>

<style>

</style>