<template>
  <div class="list row shadow p-3">
    <div class="col-md-12">
      <div class="list row mb-2">
        <div class="col-md-6">
          <h4>Users List</h4>
        </div>
        <div class="col-md-6">
              <b-button v-b-modal.create-user-modal variant="primary">
                <b-icon icon="plus" aria-hidden="true"></b-icon>Create
              </b-button>
              <b-button variant="danger align-right ml-3">
                <b-icon icon="trash-fill" aria-hidden="true"></b-icon>Delete All
              </b-button> 
        </div>
      </div>
    </div>
    <div class="col-md-12">
      <b-table 
        id="users-table"
        striped
        hover
        :items="users"
        :fields="fields"
        :per-page="perPage"
        :current-page="currentPage"
        show-empty
      >
        <template #cell(index)="data">
          {{ ((currentPage-1) * perPage)+(data.index + 1) }}
        </template>
        <template #cell(delete)="data">
          <a @click="selectedUser=data.item" v-b-modal.confirmation-modal>
            <b-icon icon="trash-fill" variant="danger" aria-hidden="true"></b-icon>
          </a>
        </template>
        <template #cell(edit)="data">
          <a @click="selectedUser=data.item" v-b-modal.confirmation-modal>
            <b-icon icon="pencil-fill" variant="primary" aria-hidden="true"></b-icon>
          </a>
        </template>
      </b-table>
      <b-pagination
        v-model="currentPage"
        :total-rows="rows"
        :per-page="perPage"
        aria-controls="users-table"
        ></b-pagination>
    </div>
    
    <CreateUserModal
      v-on:initiateCreate="createUser"
    ></CreateUserModal>
   
    <Confirmation
      v-on:confirmationOk="deleteUser"
      v-bind:user="selectedUser"
    ></Confirmation>

  </div>
</template>

<script>
import UserDataService from "../services/UserDataService";
import Confirmation from "../components/modal/Confirmation";
import CreateUserModal from "../components/modal/CreateUserModal";

export default {
  name: "users-list",
  data() {
    return {
      selectedUser:{"id":null,"email":null},
      users: [],
      fields: ["index","name", "email","delete","edit"],
      currentPage: 1,
      perPage: 3,
    };
  },
  components:{
    Confirmation,
    CreateUserModal
  },
  methods: {
    retrieveUsers() {
      UserDataService.getAll()
        .then(response => {
          this.users = response.data;
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    },
    createUser(name,email){
      const body = {'name':name,'email':email}
      UserDataService.create(body)
        .then(response => {
          //this.users = response.data;
          this.retrieveUsers();
          this.makeToast('success',`Created user ${this.name}`, 'Success')
          console.log(response.data);
        })
        .catch(e => {
          this.makeToast('danger',e.response.data.message, 'Failed')
          console.log(e);
        });
      this.$nextTick(() => {
          this.$bvModal.hide('create-user-modal')
      })
    },
    deleteUser(){
      UserDataService.delete(this.selectedUser._id.$oid)
        .then(response => {
          //this.users = response.data;
          this.retrieveUsers();
          this.makeToast('success',`Deleted user ${this.selectedUser.name}`, 'Success')
          console.log(response.data);
        })
        .catch(e => {
          this.makeToast('danger',`Couldn't delete user ${this.selectedUser.name}`, 'Failed')
          console.log(e);
        });
      this.$nextTick(() => {
          this.$bvModal.hide('confirmation-modal')
      })
    },
    makeToast(variant = null, message = null, title=null) {
        this.$bvToast.toast(`${message || 'Failed'}`, {
          title: `${title || 'Failed'}`,
          variant: variant,
          autoHideDelay: 5000,
          appendToast: true
        })
      }

  },
  computed: {
      rows() {
        return this.users.length
      }
  },
  mounted() {
    this.retrieveUsers();
  }
};
</script>

<style>
.list {
  text-align: left;
  max-width: 750px;
  margin: auto;
}
</style>
