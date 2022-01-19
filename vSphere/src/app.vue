<template>
  <div id="app">
    <Headerbar />
    <div class="main-section columns">
      <Navigation />
      <main class="column">
        <router-view />
      </main>
    </div>
  </div>
</template>


<script>
import Headerbar from '@/components/Header/Header.vue'
import Navigation from '@/components/NavigationBar/Navigation.vue'
export default{
   components: { 
     Headerbar,
     Navigation
  },
};
</script>

<style lang="scss">
@import '@/design/index.scss';
</style>
