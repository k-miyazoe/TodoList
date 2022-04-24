<template>
  <v-container grid-list-md>
    <v-layout row wrap align-center justify-center fill-height>
      <v-flex xs12 sm8 lg4 md5>
        <v-card class="login-card">
          <v-card-title>
            <span class="headline">ユーザー情報</span>
          </v-card-title>

          <v-spacer />

          <v-card-text>
            <v-layout
              row
              fill-height
              justify-center
              align-center
              v-if="loading"
            >
              <v-progress-circular :size="50" color="primary" indeterminate />
            </v-layout>

            <v-form v-else ref="form" v-model="valid" lazy-validation>
              <v-container>
                <v-text-field
                  v-model="credentials.name"
                  :counter="20"
                  label="アカウント名"
                  :rules="rules.name"
                  maxlength="20"
                  required
                />
                <v-text-field
                  v-model="credentials.email_address"
                  :counter="70"
                  label="メールアドレス"
                  :rules="rules.email_address"
                  maxlength="70"
                  required
                />
                <v-select
                  v-model="credentials.best_contact"
                  :items="contacts"
                  label="お気に入りの連絡手段"
                  required
                />
                <v-select
                  v-model="credentials.now_state"
                  :items="states"
                  label="現在の状態"
                  required
                ></v-select>
                <v-select
                  class="mx-2"
                  v-model="credentials.dev_experiece"
                  :items="languages"
                  attach
                  chips
                  label="言語"
                  multiple
                ></v-select>

                <v-checkbox
                  v-model="credentials.active_type"
                  label="朝型"
                  value="false"
                ></v-checkbox>
                <v-checkbox
                  v-model="credentials.active_type"
                  label="夜型"
                  value="true"
                ></v-checkbox>
              </v-container>
              <v-btn
                class="pink white--text"
                :disabled="!valid"
                @click="postUserInfo()"
                >登録</v-btn
              >
            </v-form>
            <v-btn @click="getUserInfo()">Get</v-btn>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import axios from "axios";
import Swal from "sweetalert2";
import router from "../router";
export default {
  name: "UserInfo",
  data: () => ({
    credentials: {},
    valid: true,
    loading: false,
    //rulesはフレームワークの機能以上のことをしたい時にかくもの
    rules: {
      name: [
        (v) => !!v || "ユーザー名は必須です",
        (v) =>
          (v && v.length > 4) || "ユーザー名は5文字以上でなければなりません",
        //v => /^[a-z0-9_]+$/.test(v) || "許可されていない文字が入力されています"
      ],
      email_address: [(v) => !!v || "emailアドレスは必須です"],
    },
    best_contact: "",
    contacts: ["LINE", "email", "Teams", "discode", "zoom"],
    now_state: "",
    states: ["忙しい", "普通", "忙しくない"],
    dev_experiece: "",
    languages: [
      "C",
      "C#",
      "C++",
      "CSS",
      "Go",
      "HTML",
      "Java",
      "Javascript",
      "Kotlin",
      "Objective-C",
      "PHP",
      "PHP",
      "Perl",
      "Python",
      "R",
      "Ruby",
      "SQL",
      "Scala",
      "Swift",
      "TypeScript",
      "特になし",
    ],
    active_type: false,
    level_of_skill: "",
  }),
  mounted() {
    this.checkLoggedIn();
  },
  methods: {
    postUserInfo() {
      console.log("確認", this.credentials);
      //フォームに正しく入力した場合
      if (this.$refs.form.validate()) {
        this.loading = true;
        axios
          .post(
            process.env.VUE_APP_API_URL + "/api/post_my_user/",
            this.credentials
          )
          .then((res) => {
            console.log(res);
            this.loading = false;
          })
          .catch((e) => {
            this.loading = false;
            console.log(e);
            Swal.fire({
              icon: "warning",
              title: "Error",
              showConfirmButton: false,
              showCloseButton: false,
              timer: 3000,
            });
          });
      }
    },
    getUserInfo() {
      axios
        .get(process.env.VUE_APP_API_URL + "/api/get_my_user")
        .then((res) => {
          console.log(res);
        })
        .catch((e) => {
          console.log(e);
        });
    },
    checkLoggedIn() {
      this.$session.start();
      if (!this.$session.has("token")) {
        router.push("/auth");
      }
    },
  },
};
</script>