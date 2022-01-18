import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

// Importing BootStrap
import "bootstrap/dist/css/bootstrap.css"
import "bootstrap-vue/dist/bootstrap-vue.css"
import "bootswatch/dist/flatly/bootstrap.min.css";
//Importing FontAwesome
import '@fortawesome/fontawesome-free/js/all'


createApp(App).use(store).use(router).mount("#app");
