import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import routes from './router.js'
import axios from 'axios'
import Vuetify from 'vuetify';
import VeeValidate, {Validator} from 'vee-validate'
import Rules from './rules.js'

import 'vuetify/dist/vuetify.min.css'
import 'material-design-icons-iconfont/dist/material-design-icons.css'

Vue.use(VueRouter)
Vue.use(Vuetify)
Vue.use(VeeValidate, {
  errorBagName: 'FormErrors',
  locale: 'en',
  }
)
Rules(Validator)


Vue.prototype.appsApi = axios.create({
  baseURL: process.env.VUE_APP_API_URL,
  timeout: 110000,
});


Vue.config.productionTip = false

new Vue({
  router: routes,
  render: h => h(App),
}).$mount('#app')