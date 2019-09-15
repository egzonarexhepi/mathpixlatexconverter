<template>
  <div class="about">
    <p class="text-break" style="max-width: 4rem;"></p>
    <h1 class="text-center">Mathpix Latex Expansion</h1>

    <p class="text-break" style="max-width: 4rem;"></p>
    <p class="text-center">Created for Hophacks Fall 2019.</p>
    <p class="text-center">Created by Egzona Rexhepi, Mareesh Kumar Issar, Matthew Yang, Yiwen Yu.</p>

    <v-container fluid>
      <v-row justify="center">
        <v-col cols="10">
          <v-row :align="alignment" :justify="justify" style="weight:250px">
            <v-card v-for="n in 1" :key="n" class="ma-3 pa-6" outlined tile>
              <p
                class="font-weight-light"
              >The purpose of this repo is to fulfill the Mathpix challenge to expand mathpix snip technology. Mathpix snip is a technology which processes handwritten or digitally printed advanced mathematical expressions and extracts Latex code from them. This process expands on mathpix snip technology to process larger data sets, like whole pages or several pages, rather than just a few lines which must be manually cropped (the current working stage of mathpix snip).</p>

              <p
                class="font-weight-light"
              >This project was created using publicly available APIs and Mathpix API found here: http://docs.mathpix.com</p>

              <p
                class="font-weight-light"
              >This application was built using Flask and Vue.js frameworks to showcase our Mathpix challenge. The Mathpix challenge was solved using a Google Cloud Vision Machine Learning API, Crop Hints, which was customized to allow for optimal cropping for any pdf document. So, larger data sets are deconstructed using Crop Hints, processed by existing Mathpix technology, and then the extracted LaTeX code is reconstructed.</p>
            </v-card>
          </v-row>
        </v-col>
        <v-col cols="12">
          <v-row justify="center"></v-row>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>
