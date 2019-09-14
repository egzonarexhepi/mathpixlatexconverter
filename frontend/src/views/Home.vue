<template>
  <div class="home">
     <v-jumbotron>
      <v-container fill-height>
        <v-layout justify-center>
          <v-spacer></v-spacer>
          <v-flex>
            <h3 class="display-3">{{msg}}</h3>
            <v-btn justify-center large color="primary" class="mx-0">Upload pdf</v-btn>
          </v-flex>
        </v-layout>
      </v-container>
    </v-jumbotron>
  </div>
</template>

<script>
export default {
  name: "App",
  data: () => ({
    msg: "Mathpix snip",
  })
};
</script>