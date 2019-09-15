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

    <v-container>
      <v-row justify="center">
        <v-col cols="6" md="4">
          <v-card class="pa-2" outlined tile>
            <v-img height="400" width="500" src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"></v-img>
          </v-card>
        </v-col>
        <v-col cols="6" md="4">
          <v-card class="pa-2" outlined tile>
            <v-img height="400" width="500" src="https://cdn.vuetifyjs.com/images/cards/store.jpg"></v-img>
          </v-card>
        </v-col>
      </v-row>
    </v-container>

    <v-card max-width="600" class="mx-auto">
      <v-card-title>LaTeX</v-card-title>
      <v-card-text>
        <v-row no-gutters>
          <template v-for="n in 4">
            <v-col :key="n">
              <v-card class="pa-4" outlined tile>Column</v-card>
            </v-col>
            <v-responsive v-if="n === 2" :key="`width-${n}`" width="100%"></v-responsive>
          </template>
        </v-row>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
export default {
  name: "App",
  data: () => ({
    media: true,
    msg: "Mathpix snip"
  })
};
</script>
