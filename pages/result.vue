<template>
    <main>
        <h1>Resultado:</h1>
        <p>Tienes: {{query.disease || 'No tienes nada we'}}</p>
        <NuxtLink to="/">Regresar</NuxtLink>
    </main>
</template>

<script setup lang="ts">

    definePageMeta({
        pageTransition: {
            name: 'slide-left',
            mode: 'out-in'
        },
    })
    const { query } = useRoute()

</script>

<style scoped>
main{
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}
h1{
    color: #00B295;
}
a{
    background-color: #F1064A;
    color: white;
    padding: 8px 18px;
    border: 0;
    font-size: large;
    border-radius: 4px;
    margin: auto;
    text-decoration: none;
    margin: 20px;
}
</style>

<style>
.slide-left-enter-active,
.slide-left-leave-active,
.slide-right-enter-active,
.slide-right-leave-active {
  transition: all 0.2s;
}
.slide-left-enter-from {
  opacity: 0;
  transform: translate(50px, 0);
}
.slide-left-leave-to {
  opacity: 0;
  transform: translate(-50px, 0);
}
.slide-right-enter-from {
  opacity: 0;
  transform: translate(-50px, 0);
}
.slide-right-leave-to {
  opacity: 0;
  transform: translate(50px, 0);
}
</style>