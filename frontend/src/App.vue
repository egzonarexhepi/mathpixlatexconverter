<template>
  <v-app>
    <v-app-bar app>
      <v-toolbar-title class="headline text-uppercase">
        <span>mathpix</span>
        <span class="font-weight-light">snip </span>
        <span>challenge</span>
      </v-toolbar-title>

      <v-layout justify-end align-center>
        <li>
          <router-link to="/">
          <v-icon 
            color="primary"
            class="ma-md-2" 
          >
            mdi-home
          </v-icon>
          </router-link>
        </li>

        <li>
          <router-link class="mt-md-2" color="black" to="/about">About</router-link>
        </li>
      </v-layout>
    </v-app-bar>

    <v-content transition="slide-x-transition">
      <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script>
export default {
  name: "App",
  data: () => ({
    //
  })
};
</script>

<style scoped>
  li a{
    text-decoration: none;
  }
</style>