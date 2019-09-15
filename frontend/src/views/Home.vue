<template>
  <div class="home">
      <v-container>
      <v-layout row class="pa-md-6">
          <v-flex md12>
            <div class="text-md-center">
              <h3 class="display-3" 
              font-weight:bold>
              Mathpix snip</h3>
            </div>
      </v-layout>


      <v-layout row class="pa-md-6">
        <v-flex md12>
          <div class="text-md-center">

              <v-btn 
                large 
                color="primary" 
                class="ma-sm-4" 
                @click="openFileDialog"
              >
                Upload
                <v-icon right dark> mdi-cloud-upload</v-icon>
              </v-btn>
              <input 
                type="file" 
                id="file-upload" 
                style="display:none" 
                @change="onFileChange"
              >

              <v-btn large text color="primary">Extract</v-btn>

          </div>
        </v-flex>
      </v-layout>


      </v-container>

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
    formData: new FormData(),
  }),

  methods : {
    openFileDialog(){
      document.getElementById('file-upload').click();
    },
    onFileChange(e) {
      const vm = this;
      var files = e.target.files || e.dataTransfer.files;       
      if(files.length > 0){
        for(var i = 0; i< files.length; i++){
            vm.formData.append("file", files[i], files[i].name);
        }
      }
      console.log(vm.formData);
    },
    uploadFile() {
      const vm = this; 
      axios.post('URL', vm.formData).then(function (response) {
          console.log(response);
      }).catch(function (error) {
          console.log(error);
      });
      console.log(JSON.stringify(vm.formData));
    },
  }
};
</script>


<style>
@import url('https://fonts.googleapis.com/css?family=Open+Sans&display=swap');

.b6{
  font-family: 'Open Sans', sans-serif;
}
</style>
