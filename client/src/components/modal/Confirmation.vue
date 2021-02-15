<template>
    <b-modal 
      id="confirmation-modal"
      title="Delete User(s)"
      ref="modal"
      @ok="confirmationOk"
      >
      <p v-if="user.email" class="my-4">Are you sure you want to delete the user: {{user.email}}</p>
      <p v-else class="my-4">Are you sure you want to delete all the users</p>
    </b-modal>
</template>

<script>
export default {
  name: "confirmation",
  props: ['user'],
  methods: {
    confirmationOk() {
      this.$emit('confirmationOk');
    }
  }
};
</script>
