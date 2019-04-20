import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "home",
      component: () => import("@/views/Home.vue")
    },
    {
      path: "/about",
      name: "about",
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("./views/About.vue")
    },
    {
      path: "/user/:id",
      name: "user-edit",
      component: () => import("./views/UserEdit.vue")
    },
    {
      path: "/add",
      name: "add",
      component: () => import("@/views/UserAdd.vue")
    }
  ]
});
