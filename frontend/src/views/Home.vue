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
          </v-flex>
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
                ref="file"
                style="display:none" 
                v-on:change="handleFileUpload()"
              >
              <v-btn large text color="primary">Extract</v-btn>
          </div>
        </v-flex>
      </v-layout>


      </v-container>

    <v-container>
      <v-row justify="center">
        <v-col cols="6" md="4">
          <v-card height="420" width="550" class="pa-2" outlined tile>
            <PDFDocument v-bind="{url, scale}" />            
              <v-img contain height="400" width="500" v-show="showPreview" :src="imagePreview"></v-img>
          </v-card>
        </v-col>
        <v-col cols="6" md="4">
          <v-card height="420" width="550" class="pa-2" outlined tile>
            <!--IDK-->
          </v-card>
        </v-col>
      </v-row>
    </v-container>

    <v-card max-width="600" class="mx-auto mt-md-10 mb-md-10">
      <v-card-title>
        <div class="text-center">
          <v-btn 
            text
            :class="{isblack : lat}"
            @click="buttonChange"
          >
            Latex
          </v-btn>
        </div>  
        <div class="text-center">
          <v-btn 
            text
            :class="{isblack : ur}"
            @click="buttonChange"
          >
            URLs
          </v-btn>
        </div>  
      </v-card-title>
      <v-card-text>
          <v-data-table
            :headers="headers"
            :items="entries"
            :pagination.sync="pagination"
            hide-default-header
            class="elevation-1"
            :loading="loading"
            :footer-props="{
              'items-per-page-options': [4,8]
            }"
            :items-per-page="4"
          >
          </v-data-table>

      </v-card-text>
    </v-card>

    <v-container>
      Confidence
      <v-layout justify-center class="md6 mb-md-10">
        <v-progress-linear
          :active="true"
          :bottom="false"
          :buffer-value="100"
          :height="4"
          :indeterminate="false"
          :query="false"
          :rounded="false"
          :stream="false"
          :striped="false"
          :top="top"
          :value=confidence
          color="success"
        ></v-progress-linear>
      </v-layout>
    </v-container>

  </div>
</template>

<script>

export default {
  name: "App",
  data: () => ({
    file: '',
    showPreview: false,
    imagePreview: '',
    confidence: 70,
    lat: true,
    ur: false,
    formData: new FormData(),
    pagination: {
     rowsPerPage: 4
    },
    rowsPerPageItems: [4, 8],
    headers: [
      { text: 'Category', value: 'category' }
    ],
    entries: [
      {
        category: "1"
      },
      {
        category: "2"
      },
      {
        category: "3"
      },
      {
        category: "4"
      }
    ],
  }),

  methods : {
    openFileDialog(){
      document.getElementById('file-upload').click();
    },
    handleFileUpload(){
      this.file = this.$refs.file.files[0];
      let reader  = new FileReader();
      reader.addEventListener("load", function () {
        this.showPreview = true;
        this.imagePreview = reader.result;
      }.bind(this), false);
    
      if( this.file ){
        reader.readAsDataURL( this.file );
        }
    },
    buttonChange(){
      const vm = this;
      vm.ur = !vm.ur;
      vm.lat = !vm.lat;
    }
  },

    // onFileChange(e) {
    //   const vm = this;
    //   var files = e.target.files || e.dataTransfer.files;       
    //   if(files.length > 0){
    //     for(var i = 0; i< files.length; i++){
    //         vm.formData.append("file", files[i], files[i].name);
    //     }
    //   }
    //   console.log(vm.formData);
    // },
    // uploadFile() {
    //   const vm = this; 
    //   axios.post('URL', vm.formData).then(function (response) {
    //       console.log(response);
    //   }).catch(function (error) {
    //       console.log(error);
    //   });
    //   console.log(JSON.stringify(vm.formData));
    // },
    //}
};
</script>


<style>
@import url('https://fonts.googleapis.com/css?family=Open+Sans&display=swap');

.b6{
  font-family: 'Open Sans', sans-serif;
}
.isgrey{
  color:lightslategray;
}
.isblack{
  color:black;
}
</style>
