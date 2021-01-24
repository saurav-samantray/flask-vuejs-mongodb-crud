<template>
    <b-modal 
      id="confirmation-modal"
      title="Delete User"
      ref="modal"
      @ok="confirmationOk"
      >
      <p class="my-4">Are you sure you want to delete the user: {{user.name}}</p>
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
