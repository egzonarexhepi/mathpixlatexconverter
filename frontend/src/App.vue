<template>
  <v-app>
    <v-app-bar app>
      <v-toolbar-title class="headline text-uppercase">
        <span>mathpix</span>
        <span class="font-weight-light">snip</span>
        <span>challenge</span>
      </v-toolbar-title>
    </v-app-bar>

    <v-content>
      <HelloWorld/>
    </v-content>
  </v-app>
</template>

<script>
import HelloWorld from './components/HelloWorld';

export default {
  name: 'App',
  components: {
    HelloWorld,
  },
  data: () => ({
    //
  }),
};
</script>
