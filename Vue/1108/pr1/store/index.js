import Vue from "vue";
import Vuex from "vuex";

/*
// 기능별 분리
import state from "./state.js";
import mutations from "./mutation.js";
import actions from "./actions.js";

export default new Vuex.Store({
  state,
  mutations,
  actions,
  getters: {},
});
*/
import state from "@/store/modules/todo.js";

Vue.use(Vuex);

export default new Vuex.Store({
  state: { ...state()
  },
  mutations: {
  },
  actions: {
  },
  getters: {
  },
  modules: {},
});
