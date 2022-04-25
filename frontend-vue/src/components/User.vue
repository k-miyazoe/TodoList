<template>
  <div>
    <div v-if="loading">
      <h1>loading</h1>
    </div>
    <div v-else>
      <v-container>
        <v-row align="center" justify="space-around">
          <v-btn depressed @click="log_test()"> View Log </v-btn>
          <v-btn depressed color="primary" @click="get_Userdata_all()">
            Get All Users
          </v-btn>
          <v-btn depressed color="error" @click="get_Userdata('1')">
            Get User 1
          </v-btn>
        </v-row>
        <!--ユーザー情報入力form-->
        <v-form v-model="valid">
          <v-container>
            <v-row>
              <v-col cols="12" md="4">
                <v-text-field
                  v-model="user_info.name"
                  :counter="20"
                  label="アカウント名"
                  :rules="rules.name"
                  maxlength="20"
                  required
                />
                <v-text-field
                  type="password"
                  v-model="user_info.password"
                  :counter="20"
                  label="パスワード"
                  :rules="rules.password"
                  maxlength="20"
                  required
                  v-on:keydown.enter="post_CreateUser"
                />
                <v-btn @click="post_CreateUser()">Create User</v-btn>
              </v-col>
            </v-row>
          </v-container>
        </v-form>
      </v-container>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
import Axios from "axios";
import Cookies from "js-cookie";
//env_files/front.env
//const ENV_PATH = path.join(__dirname, ".env");
//require("dotenv").config({ path: ENV_PATH });

export default {
  data: () => ({
    user_object: [],
    loading: false,
    user_info: {},
    valid: false,
    rules: {
      username: [
        (v) => !!v || "ユーザー名は必須です",
        (v) =>
          (v && v.length > 4) || "ユーザー名は5文字以上でなければなりません",
        (v) =>
          /^[a-z0-9_]+$/.test(v) || "許可されていない文字が入力されています",
      ],
      password: [
        (v) => !!v || "パスワードは必須です",
        (v) =>
          (v && v.length > 4) || "パスワードは5文字以上でなければなりません",
      ],
    },
  }),
  methods: {
    log_test() {
      console.log("env_0", process.env);
      console.log("env", process.env.VUE_APP_API_URL);
      //console.log("jwt", this.$session.get("token"));
    },
    get_Userdata(parameter) {
      const axios = Axios.create({
        baseURL: process.env.VUE_APP_API_URL,
        timeout: 2500,
        headers: {
          Authorization: `JWT ${this.$session.get("token")}`,
        },
      });
      axios
        .get("/api/users/" + parameter)
        .then((res) => {
          console.log(res);
        })
        .catch((e) => {
          console.log(e);
        });
    },
    get_Userdata_all() {
      const axios = Axios.create({
        baseURL: process.env.VUE_APP_API_URL,
        timeout: 2500,
        headers: {
          Authorization: `JWT ${this.$session.get("token")}`,
        },
      });
      axios
        .get("/api/users/")
        .then((res) => {
          console.log(res.data);
        })
        .catch((e) => {
          console.log(e);
        });
    },
    post_CreateUser() {
      const csrftoken = Cookies.get("csrftoken");
      console.log("jwt", this.$session.get("token"));
      const axios = Axios.create({
        baseURL: process.env.VUE_APP_API_URL,
        timeout: 2500,
        headers: {
          "Content-Type": "application/json",
          Authorization: `JWT ${this.$session.get("token")}`,
          "X-CSRFToken": csrftoken,
        },
      });
      let create_object = {
        username: this.user_info.name,
        password: this.user_info.password,
      };
      axios
        .post("/api/create-users/", create_object)
        .then((res) => {
          console.log(res.data);
          (this.user_info.name = ""), (this.user_info.password = "");
        })
        .catch((e) => {
          console.log(e);
        });
    },
  },
};
</script>