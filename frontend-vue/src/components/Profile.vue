<template>
  <v-app id="inspire">
    <v-main class="grey lighten-2">
      <v-container>
        <v-row align="center">
          <!-- プロフィール画像部分 -->
          <v-col cols="3" sm="4">
            <img
              class="profile_img"
              src="../assets/IMG_0152.jpeg"
              alt="me文字"
            />
            <!-- ユーザネーム start-->
            <div class="hidden-sm-and-down">
              <p class="display-1 font-weight-bold">{{ user_profile.name }}</p>
              <!-- プロフィール編集 -->
              <v-dialog v-model="dialog" width="700">
                <template v-slot:activator="{ on, attrs }">
                  <v-btn
                    class="mt-2 rounded-xl"
                    block
                    v-bind="attrs"
                    v-on="on"
                    @click="init_profile()"
                  >
                    edit profile
                    <v-icon right> mdi-pencil </v-icon>
                  </v-btn>
                </template>

                <v-card>
                  <v-card-title class="text-h5 grey lighten-2">
                    プロフィール編集
                  </v-card-title>

                  <v-row>
                    <v-col>
                      <v-form ref="form" v-model="valid" lazy-validation>
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
                        />
                        <v-select
                          class="mx-2"
                          v-model="credentials.dev_experiece"
                          :items="languages"
                          attach
                          chips
                          label="言語"
                          multiple
                        />
                        <v-checkbox
                          v-model="credentials.active_type"
                          label="朝型"
                          value="false"
                        />
                        <v-checkbox
                          v-model="credentials.active_type"
                          label="夜型"
                          value="true"
                        />
                      </v-form>
                    </v-col>
                  </v-row>

                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="red" text @click="dialog = false"
                      >close</v-btn
                    >
                    <!--postにする-->
                    <v-btn
                      color="primary"
                      text
                      @click="(dialog = false), postUserInfo()"
                    >
                      save
                    </v-btn>
                  </v-card-actions>
                </v-card>
              </v-dialog>
            </div>
            <!--ユーザーネーム end-->
          </v-col>
          <v-col class="hidden-md-and-up" cols="8">
            <p class="display-1 font-weight-bold">{{}}</p>
          </v-col>

          <!-- 右側 プロフィール部分 -->
          <v-col class="mt-n3">
            <div>
              <v-card class="rounded-xl">
                <v-col align="center">
                  <v-list-item>
                    <v-list-item-content>
                      <v-list-item-title class="font-weight-bold"
                        >プロフィール</v-list-item-title
                      >
                    </v-list-item-content>
                  </v-list-item>
                </v-col>

                <v-divider></v-divider>
                <!--ユーザーのemail-->
                <v-list-item>
                  <v-col align="start" cols="3">
                    <v-icon> mdi-email </v-icon>
                  </v-col>
                  <v-col align="start">
                    <v-list-item-content>
                      <v-list-item-subtitle>
                        {{ user_profile.email_address }}
                      </v-list-item-subtitle>
                    </v-list-item-content>
                  </v-col>
                </v-list-item>
                <v-divider></v-divider>
                <!--ユーザーの得意領域 DBになし-->
                <v-list-item>
                  <v-col align="start" cols="3">
                    <v-icon> mdi-cog </v-icon>
                  </v-col>
                  <v-col align="start">
                    <v-list-item-content>
                      <v-chip-group>
                        <v-list-item-subtitle>
                          <!--得意分野はdbにないので表示されない-->
                          <v-chip
                            small
                            v-for="field in user_field"
                            :key="field"
                          >
                            {{ field }}
                          </v-chip>
                        </v-list-item-subtitle>
                      </v-chip-group>
                    </v-list-item-content>
                  </v-col>
                </v-list-item>
                <v-divider></v-divider>
                <!--ユーザーの連絡手段-->
                <v-list-item>
                  <v-col align="start" cols="3">
                    <v-icon> mdi-phone-log </v-icon>
                  </v-col>
                  <v-col align="start">
                    <v-list-item-content>
                      <v-list-item-subtitle>
                        {{ user_profile.best_contact }}
                      </v-list-item-subtitle>
                    </v-list-item-content>
                  </v-col>
                </v-list-item>
                <v-divider></v-divider>
                <!--ユーザーの忙しさ-->
                <v-list-item>
                  <v-col align="start" cols="3">
                    <v-icon> mdi-hand-extended-outline </v-icon>
                  </v-col>
                  <v-col align="start">
                    <v-list-item-content>
                      <v-list-item-subtitle>
                        {{ user_profile.now_state }}
                      </v-list-item-subtitle>
                    </v-list-item-content>
                  </v-col>
                </v-list-item>
                <v-divider></v-divider>
                <!--ユーザーの使用言語-->
                <v-list-item>
                  <v-col align="start" cols="3">
                    <v-icon> mdi-xml </v-icon>
                  </v-col>
                  <v-col align="start">
                    <v-list-item-content>
                      <v-chip-group>
                        <v-list-item-subtitle>
                          {{ user_dev }}
                        </v-list-item-subtitle>
                      </v-chip-group>
                    </v-list-item-content>
                  </v-col>
                </v-list-item>
              </v-card>
              <!-- プロフィール編集 -->
              <div class="hidden-md-and-up">
                <v-btn
                  class="mt-2 rounded-xl"
                  block
                  @click="(dialog = true), init_profile()"
                >
                  edit profile
                  <v-icon right> mdi-pencil </v-icon>
                </v-btn>
              </div>
              <v-btn class="mt-2 rounded-xl" block @click="getUserInfo()">
                get
              </v-btn>
            </div>
          </v-col></v-row
        >
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import axios from "axios";
import Swal from "sweetalert2";
export default {
  data: () => ({
    credentials: {},
    valid: true,
    loading: false,
    rules: {
      name: [
        (v) => !!v || "ユーザー名は必須です",
        (v) =>
          (v && v.length > 4) || "ユーザー名は5文字以上でなければなりません",
        (v) =>
          /^[a-z0-9_]+$/.test(v) || "許可されていない文字が入力されています",
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
    user_profile: {},
    user_dev: ["Web"],

    test: null,
    dialog: false,
    panel: null,
    tab: null,
    items: ["回答待ち", "回答済み", "メンション"],
    fields: [
      "Web",
      "ゲーム",
      "iOS",
      "Android",
      "DeepLearning",
      "ブロックチェーン",
      "自動化",
      "IoT",
    ],
    question_list: {
      回答待ち: { is_new: 0, value: ["0_hello", "0_hoge"] },
      回答済み: { is_new: 2, value: ["1_hello", "1_hoge"] },
      メンション: { is_new: 2, value: ["2_hello", "2_hoge"] },
    },

    //デフォルトのデータ
    //ダミーデータに変更する
    user_name: "山本 錦之介",
    display_user_email: "18233060@edu.cc.saga-u.ac.jp",
    user_email: "18233060@edu.cc.saga-u.ac.jp",
    display_user_lang: ["Python"],
    user_language: ["Python"],
    display_user_field: ["Web"],
    user_field: ["Apex"],
  }),
  mounted() {
    this.getUserInfo();
  },

  methods: {
    test_method() {
      this.test = this.languages.sort();
    },
    // 確認したタブのバッジを削除する
    check_tab() {
      this.question_list[this.items[this.tab]]["is_new"] = 0;
      // TODO : DBに見たことを記すデータを反映させる
    },
    // 選択した言語を追加する
    append_language(language) {
      this.user_language.push(language);
    },
    // プロフィールの初期化
    init_profile() {
      this.display_user_email = this.user_email;
      this.display_user_lang = this.user_language;
      this.display_user_field = this.user_field;
    },
    // プロフィールを保存する
    set_profile() {
      // TODO : DBにプロフィールを反映
      this.user_email = this.display_user_email;
      this.user_language = this.display_user_lang;
      this.user_field = this.display_user_field;
    },
    //動作確認ok
    postUserInfo() {
      console.log("post確認", this.credentials);
      if (this.$refs.form.validate()) {
        this.loading = true;
        axios
          .post(
            process.env.VUE_APP_API_URL + "/api/post_my_user/",
            this.credentials
          )
          .then((res) => {
            console.log("post success", res);
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
    //てきとうなユーザーデータもってくる
    getUserInfo() {
      axios
        .get(process.env.VUE_APP_API_URL + "/api/get_my_user")
        .then((res) => {
          //[]の中で特定のユーザー情報を取得できるようにしたい
          console.log(res.data[0]);
          this.user_profile = res.data[0];
          console.log(res.data[0].dev_experiece);
          this.user_dev = res.data[0].dev_experiece;
        })
        .catch((e) => {
          console.log(e);
        });
    },
  },
};
</script>

<style>
.profile_img {
  border-radius: 50%; /* 角丸半径を50%にする(=円形にする) */
  width: 80%; /* ※縦横を同値に */
  height: auto; /* ※縦横を同値に */
}
</style>
