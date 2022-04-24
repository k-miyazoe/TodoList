import Vue from "vue";
import App from "./App.vue";
import vuetify from "./plugins/vuetify";
import router from "./router";
import Vuesession from 'vue-session';

Vue.config.productionTip = false;
Vue.use(Vuesession)

new Vue({
  vuetify,
  router,
  render: (h) => h(App),
}).$mount("#app");
