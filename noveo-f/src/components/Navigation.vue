<template>
  <div>
    <v-toolbar>
      <v-toolbar-title>LOGO WAS HERE</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items class="hidden-sm-and-down">
        <v-btn flat @click="$router.push('/')">Users</v-btn>
        <v-btn flat @click="$router.push('/groups')">Groups</v-btn>
        <v-btn flat @click="$router.push('/states')">States</v-btn>
      </v-toolbar-items>
    </v-toolbar>
  </div>
</template>