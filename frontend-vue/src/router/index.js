import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Auth from "../views/Auth.vue";
import Calendar from "../components/Calendar.vue";
import Question from "../components/Question.vue";
import UserInfo from "../components/UserInfo.vue";
import TodoForm from "../components/TodoForm.vue";
import User from "../components/User.vue";

Vue.use(VueRouter);
const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/about",
    name: "About",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue"),
  },
  {
    path: "/question",
    name: "Question",
    component: Question,
  },
  {
    path: "/auth",
    name: "Auth",
    component: Auth,
  },
  {
    path: "/calendar",
    name: "Calendar",
    component: Calendar,
  },
  {
    path: "/userinfo",
    name: "UserInfo",
    component: UserInfo,
  },
  {
    path: "/todoform",
    name: "todoForm",
    component: TodoForm,
  },
  {
    path: "/user",
    name: "User",
    component: User,
  },
];

const router = new VueRouter({
  mode: 'history',
  routes,
});

export default router;
