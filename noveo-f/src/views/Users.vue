<template>
  <div>
    <template>
      <v-layout row wrap justify-end class="mt-3">
        <v-btn color="#0055ff" @click="addUser()" dark>Добавить пользователя</v-btn>
      </v-layout>
      <v-data-table
        :headers="headers"
        :items="table_data"
        hide-actions
        class="mt-4"
      >
        <template v-slot:items="props">
          <tr @click="editUser(props.item)" style="cursor: pointer">
            <td class="text-xs-left">{{ props.item.email }}</td>
            <td class="text-xs-left">{{ props.item.first_name }}</td>
            <td class="text-xs-left">{{ props.item.last_name }}</td>
            <td class="text-xs-left">{{ props.item.groups }}</td>
            <td class="text-xs-left">{{ props.item.state }}</td>
            <td class="text-xs-left">{{ props.item.date }}</td>
            <td><v-btn @click.stop @click="deleteUser(props.item.id)" icon><v-icon medium>delete</v-icon></v-btn></td>
          </tr>
        </template>
      </v-data-table>
    </template>
    <v-dialog v-model="modal.show" max-width="60%">
      <v-card>
        <v-card-title>{{ modal.title }}</v-card-title>
        <v-divider/>
        <v-container fluid>
          <form @submit.prevent="validateBeforeSubmit">
            <div class="users-form--fields">
              <v-text-field
                label="Email"
                v-model="modal.item.email"
                v-validate="modal.action === 1 ? 
                  {'required': true, 'email': true} : 
                  {'required': true, 'email': true, 'unique_user': users}"
                name="email"
                :error="(FormErrors.first('email') && submitted ? true : false)"
                :error-messages="submitted ? FormErrors.collect('email') : ''"

              />
            </div>
            <div class="users-form--fields" v-if="modal.action === 0">
              <v-text-field
                label="Password"
                v-model="modal.item.password"
                name="password"
                type="password"
                v-validate="'required'"
                :error="(FormErrors.first('password') && submitted ? true : false)"
                :error-messages="submitted ? FormErrors.collect('password') : ''"
              />
            </div>
            <div class="users-form--fields">
              <v-text-field
                label="First name"
                v-model="modal.item.first_name"
                name="first name"
                v-validate="'required'"
                :error="(FormErrors.first('first name') && submitted ? true : false)"
                :error-messages="submitted ? FormErrors.collect('first name') : ''"
              />
            </div>
            <div class="users-form--fields">
              <v-text-field
                label="Last name"
                v-model="modal.item.last_name"
                name="last name"
                v-validate="'required'"
                :error="(FormErrors.first('last name') && submitted ? true : false)"
                :error-messages="submitted ? FormErrors.collect('last name') : ''"
              />
            </div>
            <div class="users-form--fields">
              <v-autocomplete
                :items="groups"
                v-model="modal.item.groups"
                item-text="name"
                item-value="id"
                label="Group"
              />
            </div>
            <div class="users-form--fields">
              <v-autocomplete
                :items="states"
                v-model="modal.item.state"
                item-text="name"
                item-value="id"
                label="States"
              />
            </div>
            <v-layout row wrap justify-end>
              <v-btn color="grey" dark @click="modal.show = false">Отмена</v-btn>
              <v-btn color="#0055ff" dark type="submit">Сохранить</v-btn>
            </v-layout>
          </form>
        </v-container>
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
        action: 0, //0 - add new user, 1 - edit selected user
        show: false,
        item: Object.assign({}, this.emptyUser), //default state modal's items.
      },                                         //need for to reset the object in reopen Modal Window
      emptyUser: {
        email: '',
        first_name: '',
        last_name: '',
        groups: [],
        state: null
      },
      users: [],
      states: [],
      groups: [],
      table_data: [],
      submitted: false,
      headers: [
        { text: 'Email', align: 'left', value: 'email', sortable: false},
        { text: 'First name', value: 'first_name', sortable: false },
        { text: 'Last name', value: 'last_name', sortable: false },
        { text: 'Groups', value: 'groups', sortable: false },
        { text: 'State', value: 'state', sortable: false },
        { text: 'Date', value: 'date', sortable: false },
        { sortable: false },
      ],
    }
  },
  methods: {
    addUser(){
      this.modal.title = 'Добавление пользователя'
      this.modal.action = 0
      this.modal.item = Object.assign({}, this.emptyUser)
      this.modal.show = true
    },
    editUser(user){
      this.modal.title = 'Редактирование пользователя'
      this.modal.action = 1
      this.modal.item = Object.assign({}, this.users.find(origUser => origUser.id === user.id))
      this.modal.show = true
    },
    async deleteUser(id){
      try {
        const response = await this.appsApi.delete(`users/${id}`)
        await this.fetchUsers()
      } catch (err) {
        alert('ERORR! Check console')
        console.log(err)
      }
    },
    async saveUser(){
      if (this.modal.action === 0) {
        try {
          const response = await this.appsApi.post(`users/`, this.modal.item)
          await this.fetchUsers() // for get actual data.
          this.modal.show = false
        } catch (err) {
          alert('Check console')
          console.log(err)
        }
      } else if (this.modal.action === 1) {
        try {
          const response = await this.appsApi.patch(`users/${this.modal.item.id}/`, this.modal.item)
          await this.fetchUsers() // for get actual data.
          this.modal.show = false
        } catch (err) {
          alert('Check console')
          console.log(err)
        }
        
      }
    },
    async fetchUsers(){
      try {
        const response = await this.appsApi.get(`users/`)
        this.users = response.data
        this.table_data = []
        this.users.forEach(user => {
          this.table_data.push({
            id: user.id,
            email: user.email,
            first_name: user.first_name,
            last_name: user.last_name,
            date: user.date,
            groups: user.groups ? this.groups.find(group => group.id === user.groups).name : '',
            state: user.state ? this.states.find(state => state.id === user.state).name : '',
          })
        })
      } catch (err) {
        alert('Error! Check console')
        console.log(err)
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
    async fetchGroups(){
      try {
        const response = await this.appsApi.get(`groups/`)
        this.groups = response.data
      } catch (err) {
        console.log(err)
      }
    },
    validateBeforeSubmit() {
      this.submitted = true
      this.$validator.validateAll().then((result) => {
        if (result) {
          this.saveUser()
          this.submitted = false
          return
        }
      })
    }
  },
  async created() {
    await this.fetchGroups()
    await this.fetchStates()
    await this.fetchUsers()
  },
}
</script>
<style>
.users-form--fields{
  margin: 0 auto;
  width: 60%;
}
</style>

