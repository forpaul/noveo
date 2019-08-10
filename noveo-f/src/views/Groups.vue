<template>
  <div>
    <template>
      <v-layout row wrap justify-end class="mt-3">
        <v-btn color="#0055ff" @click="addGroup()" dark>Добавить группу</v-btn>
      </v-layout>
      <v-data-table
        :headers="headers"
        :items="groups"
        hide-actions
        class="mt-4"
      >
        <template v-slot:items="props">
          <tr @click="editGroup(props.item)" style="cursor: pointer">
            <td class="text-xs-left">{{ props.item.id }}</td>
            <td class="text-xs-left">{{ props.item.name }}</td>
            <td><v-btn @click.stop @click="deleteGroup(props.item.id)" icon><v-icon medium>delete</v-icon></v-btn></td>
          </tr>
        </template>
      </v-data-table>
    </template>
    <v-dialog v-model="modal.show" max-width="60%">
      <v-card>
        <v-card-title>{{ modal.title }}</v-card-title>
        <v-divider/>
        <v-container fluid>
          <div class="groups-form--fields">
            <v-text-field
              label="Name"
              v-model="modal.item.name"
            />
          </div>
        </v-container>
        <v-layout row wrap justify-end>
          <v-btn color="grey" dark @click="modal.show = false">Отмена</v-btn>
          <v-btn color="#0055ff" dark @click="saveGroup()">Сохранить</v-btn>
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
        action: 0, //0 - add new group, 1 - edit selected group
        show: false,
        item: Object.assign({}, this.emptyGroup), //default state modal's items.
      },                                         //need for to reset the object in reopen Modal Window
      emptyGroup: {
        name: '',
      },
      groups: [],
      headers: [
        { text: 'ID', align: 'left', value: 'id', sortable: false},
        { text: 'Name', value: 'name', sortable: false },
        { sortable: false },
      ],
    }
  },
  methods: {
    addGroup(){
      this.modal.title = 'Добавление группы'
      this.modal.action = 0
      this.modal.item = Object.assign({}, this.emptyGroup)
      this.modal.show = true
    },
    editGroup(group){
      this.modal.title = 'Редактирование группы'
      this.modal.action = 1
      this.modal.item = Object.assign({}, this.groups.find(origGroup => origGroup.id === group.id))
      this.modal.show = true
    },
    async deleteGroup(id){
      try {
        const reponse = await this.appsApi.delete(`groups/${id}/`)
        await this.fetchGroups()
      } catch (err) {
        alert('Error! Check console')
        console.log(err)
      }
    },
    async saveGroup(){
      if (this.modal.action === 0) {
        try {
          const response = await this.appsApi.post(`groups/`, this.modal.item)  
          alert('Группа успешно добавлена')
          this.modal.show = false
          await this.fetchGroups() // for get actual data.
        } catch (err) {
          console.log(err)
        }
      } else if (this.modal.action === 1) {
        try {
          const response = await this.appsApi.put(`groups/${this.modal.item.id}/`, this.modal.item)  
          this.modal.show = false
          await this.fetchGroups() // for get actual data.
        } catch (err) {
          alert('Error! Check console')
          console.log(err)
        }
        
      }
    },
    async fetchGroups(){
      try {
        const response = await this.appsApi.get(`groups/`)
        this.groups = response.data
      } catch (err) {
        console.log(err)
      }
    },
  },
  async created() {
    await this.fetchGroups()
  },
}
</script>
<style>
.groups-form--fields{
  margin: 0 auto;
  width: 60%;
}
</style>

