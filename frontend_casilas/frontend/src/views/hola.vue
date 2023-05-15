<template>
  <v-card>
        <v-card-title>
            Alquilar
            <!-- <v-card-subtitle> -->
                <v-row class="justify">
            <v-col-1>
                <v-btn variant="plain" >hola2</v-btn>
            </v-col-1>
            <v-col-2 align-self="end">
            <v-btn variant="plain" >hola3</v-btn>
            </v-col-2>
            <v-col-3 align-self="end">
                <v-btn
                @click="expand = !expand"
                variant="plain"
                >
                Departamento
                </v-btn>
                <v-expand-transition>
                    <v-card
                    :elevation="24"
                    v-show="expand"
                    height="100"
                    width="100"
                    class="bg-withe"
                    ></v-card>
                </v-expand-transition>
            </v-col-3>
            
            </v-row>
            <!-- </v-card-subtitle> -->
        </v-card-title>
    <v-card-text>
        <v-item-group multiple>
    <v-container>
      <v-row>
        <v-col
          v-for="n in 10"
          :key="n"
          cols="12"
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
                <div :color="blue"
                  class="flex-grow-1 text-center"
                >
                  {{ isSelected ? 'Seleccionado' : '1' }}
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
</template>
<script>
  export default {
    data: () => ({
      expand: false,
      expand2: false,
    }),
  }
</script>