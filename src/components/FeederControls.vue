<template>
  <div>
    <button @click="feedOnce">Füttern</button>
    <br>
    <br>
    <button
      @mousedown="startFeeding"
      @mouseup="stopFeeding"
    >
      Füttern (toggle)
    </button>
  </div>
</template>

<script>
export default {
  methods: {
    feedOnce() {
      fetch(`${import.meta.env.VITE_API_URL}/api/feed-once`)
        .then((response) => response.json())
        .then((data) => console.log(data));
    },
    startFeeding() {
      fetch(`${import.meta.env.VITE_API_URL}/api/start-feeding`)
        .then((response) => response.json())
        .then((data) => console.log(data));
    },
    stopFeeding() {
      fetch(`${import.meta.env.VITE_API_URL}/api/stop-feeding`)
        .then((response) => response.json())
        .then((data) => console.log(data));
    },
  },
};
</script>

<style lang="scss" scoped></style>
