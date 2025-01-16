<template>
  <div class="container">
    <TheHeader class="header" />
    <main>
      <RouterView class="main"/>
    </main>
    <TheFooter class="footer" />
  </div>
</template>
<script setup>
import TheHeader from "./components/TheHeader.vue";
import TheFooter from "./components/TheFooter.vue";
import { RouterView } from "vue-router";
</script>
