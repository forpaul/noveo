import Vue from 'vue'
import Router from 'vue-router'

import Users from './views/Users.vue'
import Groups from './views/Groups.vue'
import States from './views/States.vue'


Vue.use(Router)
const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      component: Users,
      name: 'main',
      ru_name: 'Пользователи'
    },
    {
      path: '/groups',
      component: Groups,
      name: 'products',
      ru_name: 'Группы пользователей'
    },
    {
      path: '/states',
      component: States,
      name: 'services',
      ru_name: 'Состояния пользователей'
    },
  ]
})

export default router
