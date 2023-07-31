<template>
  <v-container fluid>
    <v-row justify="center">
      <v-col cols="12" md="11">
        <v-card :elevation="4">
          <v-card-title>
            Alquilar
            <v-card-subtitle>
              <v-row class="justify-end">
                <v-col cols="auto">
                  <v-btn variant="plain">Filtro</v-btn>
                </v-col>
                <v-col cols="auto">
                  <v-btn variant="plain">Buscar</v-btn>
                </v-col>
                <v-col cols="auto">
                  <v-menu offset-y>
                    <template v-slot:activator="{ props }">
                      <v-btn v-bind="props" variant="plain" id="activator">Departamento</v-btn>
                    </template>
                    <v-list>
                      <v-list-item v-for="department in departments" :key="department" @click="selectDepartment(department)">
                        <v-list-item-title>{{ department }}</v-list-item-title>
                      </v-list-item>
                    </v-list>
                  </v-menu>
                </v-col>
              </v-row>
            </v-card-subtitle>
          </v-card-title>
          <v-card-text>
            <v-item-group v-model="selectedItems" multiple>
              <v-container>
                <v-row justify="space-between">
                  <v-col v-for="item in items" :key="item.id" cols="auto" md="1">
                    <v-item v-slot="{ isSelected, toggle }">
                      <v-card
                        :color="isSelected ? 'primary' : getItemColor(item.estado)"
                        class="d-flex align-center"
                        dark
                        height="100"
                        width="100"
                        @click="toggle"
                        :disabled="item.estado === 'Ocupado'"
                      >
                        <v-scroll-y-transition>
                          <div class="flex-grow-1 text-center">
                            {{ isSelected ? 'Seleccionado' : item.num_Casilla }}
                          </div>
                        </v-scroll-y-transition>
                      </v-card>
                    </v-item>
                  </v-col>
                </v-row>
              </v-container>
            </v-item-group>
          </v-card-text>
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
      selectedItems: [],
      expand: false,
      drawer: true,
      items: [], // Propiedad para almacenar los datos de la API
      departments: [], // Propiedad para almacenar los departamentos de la API
    };
  },
  created() {
    this.fetchData(); // Llama a la función fetchData al crear el componente
  },
  methods: {
    fetchData() {
      // Realiza una solicitud a la API para obtener los departamentos
      axios
        .get('http://172.65.14.180:8000/api/1.0/departamento/')
        .then(response => {
          this.departments = response.data.map(department => department.nombre); // Almacena los departamentos en la propiedad departments
        })
        .catch(error => {
          console.error(error);
        });

      // Realiza una solicitud a la API para obtener los datos
      axios
        .get('http://172.65.14.180:8000/api/1.0/casillas/')
        .then(response => {
          this.items = response.data; // Almacena los datos en la propiedad items
          console.log(response.data);
        })
        .catch(error => {
          console.error(error);
        });
    },
    selectDepartment(department) {
      const url = `http://172.65.14.180:8000/api/1.0/casillas/?departamento__nombre=${department}&ordering=num_Casilla`;

      axios
        .get(url)
        .then(response => {
          this.items = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    getItemColor(estado) {
      if (estado === 'Vigente') {
        return 'green';
      } else if (estado === 'Ocupado') {
        return 'red';
      }
      return '';
    },
  },
};
</script>

