// Composables
import { createRouter, createWebHistory } from 'vue-router';

const routes = [
  {
    path: '/',
    component: () => import('@/layouts/default/Default.vue'),
    children: [
      {
        path: '/casillas',
        name: 'Home',
        component: () => import('@/views/casillas.vue'),
      },
      {
        path: '',
        name: 'Login',
        component: () => import('@/views/login.vue'),
      },
      {
        path: '/register',
        name: 'register',
        component: () => import('@/views/Register.vue'),
      },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;

