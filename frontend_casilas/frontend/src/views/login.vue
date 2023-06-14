<template>
    <v-container fluid>
      <v-row justify="center" align="center">
        <v-col xs="12" sm="8" md="4">
          <v-card>
            <v-card-title class="text-center">Inicio de sesion</v-card-title>
            <v-form @submit.prevent="login">
              <v-card-text>
                <div class="text-center">
                  <v-avatar
                    color="blue"
                    size="250"
                  >
                    <v-icon size="128" color="withe" dark>
                      mdi-account
                    </v-icon>
                  </v-avatar>
                </div>
                <v-spacer></v-spacer>
                <v-text-field v-model="email" label="Nombre de usuario" ></v-text-field>
                <v-text-field v-model="password" label="Contraseña" type="password" required></v-text-field>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn type="submit" color="primary" >Iniciar session</v-btn>
                <v-spacer></v-spacer>
              </v-card-actions>
            </v-form>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="green" dark>Registrarse</v-btn>
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script>
  export default {
    data() {
      return {
        username: '',
        password: '',
      };
    },
    methods: {
      login() {
        // Lógica de inicio de sesión
      },
    },
  };
  </script>
