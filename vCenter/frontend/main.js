import Vue from "vue";
import App from "./App.vue";
import router from "./router";

import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
import BootstrapVue from "bootstrap-vue";

import { library } from "@fortawesome/fontawesome-svg-core";
import { fas } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import vuetify from "./plugins/vuetify";

Vue.config.productionTip = false;
Vue.use(BootstrapVue);
library.add(fas);
Vue.component("font-awesome-icon", FontAwesomeIcon);

new Vue({
  router,
  vuetify,
  render: (h) => h(App),
}).$mount("#app");
