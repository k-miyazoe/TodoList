<template>
  <div>
    <v-app-bar color="#00B0FF" dense dark elevation="10">
      <v-app-bar-nav-icon />
      <v-btn icon>
        <v-icon>mdi-apple</v-icon>
      </v-btn>
      <v-toolbar-title>Todolist</v-toolbar-title>
      <v-spacer />

      <!-- <v-btn icon>
        <router-link to="/question">
          <v-icon>mdi-home</v-icon>
        </router-link>
      </v-btn>
      <v-btn icon>
        <router-link to="/userinfo">
          <v-icon>mdi-account-arrow-up</v-icon>
        </router-link> -->
      <!-- </v-btn>
      <v-btn icon>
        <router-link to="/calendar">
          <v-icon>mdi-calendar-month</v-icon>
        </router-link>
      </v-btn>
      <v-btn icon>
        <router-link to="/">
          <v-icon>mdi-account</v-icon>
        </router-link>
      </v-btn> -->

      <v-menu left bottom>
        <template v-slot:activator="{ on, attrs }">
          <v-btn icon v-bind="attrs" v-on="on">
            <v-icon>mdi-dots-vertical</v-icon>
          </v-btn>
        </template>

        <!-- <v-list>
          <v-list-item>
            <v-list-item-title> docker </v-list-item-title>
            <v-btn icon>
              <v-icon>mdi-docker</v-icon>
            </v-btn>
          </v-list-item>
          <v-list-item>
            <v-list-item-title> github </v-list-item-title>
            <v-btn icon>
              <v-icon>mdi-github</v-icon>
            </v-btn>
          </v-list-item>
          <v-list-item>
            <v-list-item-title> 検索 </v-list-item-title>
            <v-btn icon>
              <v-icon>mdi-magnify</v-icon>
            </v-btn>
          </v-list-item>
          <v-list-item>
            <v-list-item-title> chat </v-list-item-title>
            <v-btn icon>
              <v-icon>mdi-chat</v-icon>
            </v-btn>
          </v-list-item>
          <v-list-item>
            <v-list-item-title> email </v-list-item-title>
            <v-btn icon>
              <v-icon>mdi-email</v-icon>
            </v-btn>
          </v-list-item>

          <v-list-item>
            <v-list-item-title> Todo </v-list-item-title>
            <v-btn icon>
              <router-link to="/todoform">
                <v-icon>mdi-application-edit-outline</v-icon>
              </router-link>
            </v-btn>
          </v-list-item>
          <v-list-item>
            <v-list-item-title> User </v-list-item-title>
            <v-btn icon>
              <router-link to="/user">
                <v-icon>mdi-account</v-icon>
              </router-link>
            </v-btn>
          </v-list-item>
        </v-list> -->
      </v-menu>
    </v-app-bar>
  </div>
</template>

<script>
</script>
