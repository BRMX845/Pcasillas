<template>
  <v-container fluid>
    <v-row justify="center">
      <v-col cols="12" sm="8" md="6">
        <v-card class="mt-5">
          <v-card-title>Registro</v-card-title>
          <div class="pa-8">
            <v-form @submit.prevent="register">
              <v-text-field label="Nombre de usuario" v-model="username" rounded variant="plain"></v-text-field>
              <v-text-field label="Correo electrónico" v-model="email" required rounded variant="plain"></v-text-field>
              <v-text-field label="Carnet de Identidad" v-model="ci" type="number" min="0" required rounded variant="plain"></v-text-field>
              <v-text-field label="Telefono celular" v-model="celular" type="number" min="0" required rounded variant="plain"></v-text-field>
              <v-text-field label="Nombre" v-model="firstName" required rounded variant="plain"></v-text-field>
              <v-text-field label="Apellido" v-model="lastName" required rounded variant="plain"></v-text-field>
              <v-autocomplete
                label="Departamento"
                v-model="selectedDepartment"
                :items="departments"
                item-text="nombre"
                item-value="nombre"
                auto-select-first
                clearable
                rounded
                variant="plain"
              ></v-autocomplete>
              <v-text-field label="Contraseña" v-model="password" type="password" required rounded variant="plain"></v-text-field>
              <v-text-field label="Confirmar contraseña" v-model="confirmPassword" type="password" required rounded variant="plain"></v-text-field>
              <v-alert v-if="error" type="error">{{ error }}</v-alert>
              <v-alert v-if="success" type="success">¡Registro exitoso!</v-alert>
              <v-card-actions class="mt-4">
                <v-spacer></v-spacer>
                <v-btn @click="register" type="submit" color="primary">Registrarse</v-btn>
                <v-spacer></v-spacer>
              </v-card-actions>
            </v-form>
          </div>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
  import axios from 'axios';

  export default {
    data() {
      return {
        departments: [],
        username: null,
        password: null,
        email: null,
        celular: null,
        ci: null,
        firstName: null,
        lastName: null,
        confirmPassword:null,
      };
    },
    created() {
      this.getDepartments();
    },
    methods: {
      getDepartments() {
        axios
          .get('http://172.65.14.246:8000/api/1.0/departamento/') // Ruta de tu API para obtener los departamentos
          .then(response => {
            this.departments = response.data.map(department => department.nombre);
          })
          .catch(error => {
            console.error(error);
          });
      },
      register() {
  // Validar contraseña
        if (this.password !== this.confirmPassword) {
          // Las contraseñas no coinciden, muestra un mensaje de error
          //this.$toast.error("Las contraseñas no coinciden");
          return; // Detener el proceso de registro
        }

        // Si las contraseñas coinciden, procede con el registro
        const userData = {
          username: this.username,
          password: this.password,
          email: this.email,
          celular: this.celular,
          ci: this.ci,
          first_name: this.firstName,
          last_name: this.lastName,
          departamento: {
            nombre: this.selectedDepartment
          }
        };

        axios
        .post('http://172.65.14.246:8000/api/1.0/Register/', userData)
        .then(response => {
          // Comprobar el código de estado de la respuesta
          if (response.status === 201) {
            // Registro exitoso
            this.success = true;
            this.error = null;
          } else {
            // Manejar otros casos de código de estado
            this.success = false;
            this.error = 'Error en el registro';
          }
        })
        .catch(error => {
          // Error durante el registro
          this.success = false;
          this.error = error.message;
          console.error(error);
        });
      },
    },
  };
</script>
