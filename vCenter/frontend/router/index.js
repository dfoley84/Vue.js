import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../components/Home.vue";
import vsphere from "../components/vsphere.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/vsphere",
    name: "vsphere",
    component: vsphere,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
