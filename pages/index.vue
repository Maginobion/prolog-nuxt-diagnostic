<template>
    <main>
        <h1>Menu</h1>
        <NuxtLink to="/diagnostic">Ir al Diagnóstico</NuxtLink>
        <NuxtLink to="/redvsarbol">Ir al Comparativo</NuxtLink>
    </main>
</template>

<script setup>
definePageMeta({
    pageTransition: {
        name: 'slide-left',
        mode: 'out-in'
    },
})
</script>

<style scoped>
main{
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    height: 100%;
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