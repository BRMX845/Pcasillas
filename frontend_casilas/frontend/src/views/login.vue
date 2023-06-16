<template>
  <v-parallax
    src="https://cdn.vuetifyjs.com/images/backgrounds/vbanner.jpg"
  >
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
                <v-text-field v-model="username" label="Nombre de usuario" ></v-text-field>
                <v-text-field v-model="password" label="Contraseña" type="password" required></v-text-field>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn type="submit" color="primary" @click="login" >Iniciar session</v-btn>
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
    </v-parallax>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        username: '',
        password: '',
      };
    },
    methods: {
      login() {
        const loginData = {
          username: this.username,
          password: this.password,
        };
  
        axios
        .post('http://172.65.14.246:8000/api/1.0/login/', loginData)
          .then(response => {
            // Guardar el token en el almacenamiento local del navegador
            localStorage.setItem('token', response.data.token);
            this.$router.push('/casillas');
          })
          .catch(error => {
            // Manejar el error de inicio de sesión
          });
      },
    },
  };
  </script>
