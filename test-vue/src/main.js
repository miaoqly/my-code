import Vue from 'vue'
import './plugins/axios'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify';
// 引用追加api接口
import api from './api/api'

Vue.config.productionTip = false
// 把api对象挂载到Vue的原形链上
// 其他界面就可以通过引用Vue引用到$api 就能引用到api中的接口
Vue.prototype.$api = api

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
