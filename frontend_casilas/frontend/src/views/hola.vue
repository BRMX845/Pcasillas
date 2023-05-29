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
                  <v-btn variant="plain">hola3</v-btn>
                </v-col>
                <v-col cols="auto">
                  <v-btn @click="expand = !expand" variant="plain">Departamento</v-btn>
                  <v-expand-transition>
                    <v-card
                      :elevation="24"
                      v-show="expand"
                      height="100"
                      width="100"
                      class="bg-withe"
                    ></v-card>
                  </v-expand-transition>
                </v-col>
              </v-row>
            </v-card-subtitle>
          </v-card-title>
          <v-card-text>
            <v-navigation-drawer v-model="drawer" right>
              <v-list dense>
                <v-list-item v-for="item in selectedItems" :key="item">
                  <v-list-item-content>{{ item }}<v-divider></v-divider></v-list-item-content>
                </v-list-item>
              </v-list>
            </v-navigation-drawer>
            <v-item-group v-model="selectedItems" multiple>
              <v-container>
                <v-row justify="space-between">
                  <v-col
                    v-for="n in 20"
                    :key="n"
                    cols="auto"
                    md="1"
                  >
                    <v-item v-slot="{ isSelected, toggle }">
                      <v-card
                        :color="isSelected ? 'primary' : ''"
                        class="d-flex align-center"
                        dark
                        height="100"
                        width="100"
                        @click="toggle"
                      >
                        <v-scroll-y-transition>
                          <div
                            :color="blue"
                            class="flex-grow-1 text-center"
                          >
                            {{ isSelected ? 'Seleccionado' : n }}
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
export default {
  data() {
    return {
      selectedItems: [],
      expand: false,
      drawer: true
    };
  }
};
</script>


