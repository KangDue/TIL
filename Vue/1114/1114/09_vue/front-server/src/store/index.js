import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '@/router/index'
Vue.use(Vuex)


export default new Vuex.Store({
  plugins:[createPersistedState(),],
  state: {
    articles:null,
    token:null,
    // articles: [
      // {
      //   id: 1,
      //   title: '제목',
      //   content: '내용'
      // },
      // {
      //   id: 2,
      //   title: '제목2',
      //   content: '내용2'
      // },
    // ],
  },
  getters: {
    isLogin(state){ //로그인 판별
      return state.token ? true:false
    }
  },
  mutations: {
    GET_ARTICLES(state,articles){
      state.articles = articles
    },
    // CREATE_ARTICLE(state,article){
    //   state.articles.push(article)
    // }
    SAVE_TOKEN(state,token) {
      state.token = token
      router.push({name:'ArticleView'})
    }
  },
  actions: {
    getArticles({commit,state}) {
      axios.get('http://127.0.0.1:8000/api/v1/articles/'
      ,	{headers:{
        Authorization: `Token ${state.token}`
      }})
      .then(res => {
        commit('GET_ARTICLES',res.data)
        
        console.log(res)
        })
      .catch(console.log)
    },
    // createArticle({commit},article) {
    //   commit('CREATE_ARTICLE',article)
    // }
    signUp(context,payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2
      
      axios({
        method:'post',
        url:'http://127.0.0.1:8000/accounts/signup/',
        data:{username,password1,password2},
      })
      .then(res => {
        context.commit('SAVE_TOKEN',res.data.key)
      })
      .catch(err => console.log(err))
    },
    logIn(context,payload) {
      const username = payload.username
      const password = payload.password
      axios({
        method:'post',
        url:'http://127.0.0.1:8000/accounts/login/',
        data:{username,password},
        headers:{
          Authorization: `Token ${context.state.token}`
        }
      })
      .then(res => {
        context.commit('SAVE_TOKEN',res.data.key)
      })
      .catch(err => console.log(err))
    }
  },
  modules: {
  }
})
