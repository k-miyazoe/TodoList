<template>
  <div>
    <v-app>
      <!--list nothing-->
      <div v-if="!todos[0]" class="mt-3">
        <v-container>
          <v-row justify="center" align-content="center">
            <v-col md="7">
              <img
                src="@/assets/well_done.jpeg"
                alt="well done"
                width="90%"
                height="auto"
              />
            </v-col>
          </v-row>
        </v-container>

        <p class="text-h5">タスクはありません</p>
        <p class="text-caption">
          タスクは下から追加できます
          <v-icon>mdi-arrow-down-thick</v-icon>
        </p>
      </div>
      <!--todo list-->
      <div v-for="(item, key) in todos" :key="key">
        <li>
          <span
            style="text-decoration: line-through; color: red"
            v-if="item.done"
            v-on:click="changeStatus(item)"
          >
            {{ item.task }}
          </span>
          <span v-else v-on:click="changeStatus(item)">
            {{ item.task }} {{ item.due }}
          </span>
          <v-btn icon color="error" @click="delete_task(item)">
            <v-icon>mdi-close-circle</v-icon>
          </v-btn>
        </li>
        <hr />
      </div>
      <!--todo form-->
      <v-form ref="form" v-model="valid" lazy-validation>
        <v-container>
          <v-row>
            <v-col cols="12" sm="6" md="3">
              <!--タスクと期日-->
              <v-text-field
                v-model="new_task"
                label="Task"
                v-on:keydown.enter="addTask"
                required
              ></v-text-field>
              <template>
                <v-row justify="space-around">
                  <v-date-picker
                    v-model="picker"
                    color="green lighten-1"
                  ></v-date-picker>
                </v-row>
              </template>
              <v-btn
                :disabled="!valid"
                color="success"
                class="mr-4"
                @click="post_task"
                >Add Task</v-btn
              >
            </v-col>
          </v-row>
        </v-container>
      </v-form>
      <button @click="test">Log</button>
    </v-app>
  </div>
</template>


<script>
/* eslint-disable */
import axios from "axios";
import Cookies from "js-cookie";
import header from "/src/js/axios";
//./js/axios

export default {
  data: () => ({
    new_task: "",
    its_due: "",
    tasks: "",
    todos: [],
    axios: {},
    valid: true,
    picker: new Date(Date.now() - new Date().getTimezoneOffset() * 60000)
      .toISOString()
      .substr(0, 10),
  }),

  mounted() {
    this.checkLoggedIn();
    this.init_axios_header();
    this.get_task();
  },

  methods: {
    checkLoggedIn() {
      this.$session.start();
      if (!this.$session.has("token")) {
        router.push("/auth");
      }
    },
    changeStatus(item) {
      console.log("update");
      item.done = !item.done;
      this.updateDB(item);
    },
    test() {
      //console.log("enter");
      console.log("export test", header.set_header());
    },

    //シリアライザー
    get_task() {
      this.axios
        .get("/api/todo/")
        .then((res) => {
          console.log(res.data);
          this.todos = res.data;
        })
        .catch((e) => {
          console.log(e);
        });
    },
    //現在badリクエスト
    post_task() {
      let task_object = this.init_task();
      this.axios
        .post("/api/todo/", task_object)
        .then((res) => {
          console.log(res.data);
        })
        .catch((e) => {
          console.log(e);
        });
      this.get_task();
    },

    //template編集
    //タスクのデザイン変更
    put_task(parameter) {
      //task_object done更新
      //putのobjectの一部更新のベストプラクティス
      update_task_object = this.init_task();
      update_task_object["done"] = true;
      this.axios
        .put("/api/todo/" + parameter, this.task_object)
        .then((res) => {
          console.log(res.data);
        })
        .catch((e) => {
          console.log(e);
        });
    },
    //template編集
    delete_task(parameter) {
      this.axios
        .delete("/api/todo/" + parameter)
        .then((res) => {
          console.log(res.data);
        })
        .catch((e) => {
          console.log(e);
        });
    },

    init_axios_header() {
      let jwt_info = `JWT ` + this.$session.get("token");
      this.axios = header.set_header(jwt_info);
      //console.log("axios header", this.axios);
    },
    init_task() {
      var task_object = {
        task: "",
        due: "",
        done: false,
      };
      task_object["task"] = this.new_task;
      task_object["due"] = this.picker + " 01:01:01";
      return task_object;
    },
  },
};
</script>
