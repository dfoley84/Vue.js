import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";

const routes = [
   {
    path: "/:pathMatch(.*)",
    name: "NotFound",
    component: () =>
      import(/* webpackChunkName: "NotFound" */ "@/components/NotFound.vue"),
  },
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/about",
    name: "About",
    component: () =>
      import(/* webpackChunkName: "About" */ "@/views/About.vue"),
  },
  {
    path: "/horizon",
    name: "Horizon",
    component: () =>
      import(/* webpackChunkName: "Horizon" */ "@/views/Horizon.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
