import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

// Importing BootStrap
import "bootstrap/dist/css/bootstrap.css"
import "bootstrap-vue/dist/bootstrap-vue.css"
import "bootswatch/dist/flatly/bootstrap.min.css";
//Importing FontAwesome
import '@fortawesome/fontawesome-free/js/all'

createApp(App).use(router).mount("#app");
