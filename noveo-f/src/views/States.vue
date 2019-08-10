<template>
  <div>
    <template>
      <v-layout row wrap justify-end class="mt-3">
        <v-btn color="#0055ff" @click="addState()" dark>Добавить состояние</v-btn>
      </v-layout>
      <v-data-table
        :headers="headers"
        :items="states"
        hide-actions
        class="mt-4"
      >
        <template v-slot:items="props">
          <tr @click="editState(props.item)" style="cursor: pointer">
            <td class="text-xs-left">{{ props.item.id }}</td>
            <td class="text-xs-left">{{ props.item.name }}</td>
            <td><v-btn @click.stop @click="deleteState(props.item.id)" icon><v-icon medium>delete</v-icon></v-btn></td>
          </tr>
        </template>
      </v-data-table>
    </template>
    <v-dialog v-model="modal.show" max-width="60%">
      <v-card>
        <v-card-title>{{ modal.title }}</v-card-title>
        <v-divider/>
        <v-container fluid>
          <div class="states-form--fields">
            <v-text-field
              label="Name"
              v-model="modal.item.name"
            />
          </div>
        </v-container>
        <v-layout row wrap justify-end>
          <v-btn color="grey" dark @click="modal.show = false">Отмена</v-btn>
          <v-btn color="#0055ff" dark @click="saveState()">Сохранить</v-btn>
        </v-layout>
      </v-card>
    </v-dialog>
  </div>
</template>
<script>
export default {
  data() {
    return {
      modal: {
        title: '',
        action: 0, //0 - add new state, 1 - edit selected state
        show: false,
        item: Object.assign({}, this.emptyState), //default state modal's items.
      },                                         //need for to reset the object in reopen Modal Window
      emptyState: {
        name: '',
      },
      states: [],
      headers: [
        { text: 'ID', align: 'left', value: 'id', sortable: false},
        { text: 'Name', value: 'name', sortable: false },
        { sortable: false },
      ],
    }
  },
  methods: {
    addState(){
      this.modal.title = 'Добавление состояния'
      this.modal.action = 0
      this.modal.item = Object.assign({}, this.emptyState)
      this.modal.show = true
    },
    editState(state){
      this.modal.title = 'Редактирование состояния'
      this.modal.action = 1
      this.modal.item = Object.assign({}, this.states.find(origState => origState.id === state.id))
      this.modal.show = true
    },
    async deleteState(id){
      try {
        const reponse = await this.appsApi.delete(`states/${id}/`)
        await this.fetchStates()
      } catch (err) {
        alert('Error! Check console')
        console.log(err)
      }
    },
    async saveState(){
      if (this.modal.action === 0) {
        try {
          const response = await this.appsApi.post(`states/`, this.modal.item)  
          this.modal.show = false
          await this.fetchStates() // for get actual data.
        } catch (err) {
          console.log(err)
        }
      } else if (this.modal.action === 1) {
        try {
          const response = await this.appsApi.put(`states/${this.modal.item.id}/`, this.modal.item)  
          this.modal.show = false
          await this.fetchStates() // for get actual data.
        } catch (err) {
          alert('Error! Check console')
          console.log(err)
        }
        
      }
    },
    async fetchStates(){
      try {
        const response = await this.appsApi.get(`states/`)
        this.states = response.data
      } catch (err) {
        console.log(err)
      }
    },
  },
  async created() {
    await this.fetchStates()
  },
}
</script>
<style>
.states-form--fields{
  margin: 0 auto;
  width: 60%;
}
</style>

