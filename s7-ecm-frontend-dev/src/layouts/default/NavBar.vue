<template>

  <v-navigation-drawer
    permanent
    location="left"
    class="bg-darkGrey"
  >
    <!--<template v-slot:prepend>

    </template>-->


    <v-img
      src="@/assets/s7-techlab.svg"
      height="40px"
      class="mt-4 mb-4"
    ></v-img>

    <div class="text-center text-caption mb-2">Engine Condition Monitoring</div>

    <v-divider />

    <v-list>
      <v-list-item
        prepend-icon="mdi-home-city"
        title="Home"
        to="/"
      ></v-list-item>

      <v-list-item
        prepend-icon="mdi-upload"
        title="Input data"
        to="/input"
      ></v-list-item>
    </v-list>
  </v-navigation-drawer>

</template>

<script setup>
//
</script>
