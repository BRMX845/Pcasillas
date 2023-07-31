<template>  
  <v-app-bar :elevation="2" color="primary">
    <!-- Título de la barra de aplicaciones -->
    <span class="ml-4">Casillas</span>
    
    <!-- Espaciador flexible que empuja el icono a la derecha -->
    <v-spacer></v-spacer>
    
    <!-- Icono "mdi-account-plus" en la parte derecha con evento de clic -->
    <v-icon @click="redirectToRegistros">mdi-account-plus</v-icon>
  </v-app-bar>
</template>

<script >
export default {
  methods: {
    redirectToRegistros() {
      // Redirigir a la ruta "/registros"
      this.$router.push('/register');
    }
  }
};
</script>

