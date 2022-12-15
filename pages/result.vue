<template>
    <main>
        <h1>Resultado:</h1>
        <div v-if="disease">
            <p>Tienes: {{enfermedadDetectada(disease)?.name}}</p>
            <p>Descripcion: {{enfermedadDetectada(disease)?.desc}}</p>
        </div>
        <p class="alive" v-else>Felicidades, estás sano</p>
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
    const disease =  query.disease as string || null

    const enfermedadDetectada = (enf:string) =>{
        if (!enf) return null
        const pos = Number(enf.slice(1,enf.length))-1
        return enfermedades[pos]
    }

    const enfermedades = [
        {
            name: "Tuberculosis",
            desc:"La tuberculosis es una enfermedad infecciosa causada por la bacteria Mycobacterium tuberculosis. Los síntomas pueden incluir tos persistente que dura más de tres semanas, dificultad para respirar o dolor en el pecho, fiebre, sudoración nocturna y pérdida de peso."
        },
        {
            name: "Neumonía",
            desc:"La neumonía es una inflamación de los pulmones causada por una infección bacteriana o viral. Los síntomas pueden incluir tos con flema, dificultad para respirar, dolor en el pecho, fiebre alta y escalofríos."
        },
        {
            name: "Bronquitis",
            desc:"La bronquitis es una inflamación de los bronquios (los tubos que llevan aire a los pulmones) causada por una infección bacteriana o viral. Los síntomas pueden incluir tos con flema, dificultad para respirar, dolor en el pecho y fiebre baja."
        },
        {
            name: "Enfisema",
            desc:"El enfisema es una enfermedad pulmonar crónica en la que se dañan los sacos de aire en los pulmones, lo que dificulta la capacidad del cuerpo para absorber oxígeno. Los síntomas pueden incluir tos crónica, dificultad para respirar, dolor en el pecho, fatiga y pérdida de peso."
        },
        {
            name: "Neumotórax",
            desc:"El neumotórax es una acumulación de aire en el espacio entre la pleura (la capa que cubre los pulmones) y el tórax (la caja torácica). Los síntomas pueden incluir dificultad para respirar, dolor en el pecho, fatiga, tos y dolor abdominal."
        },
        {
            name: "Pleuritis",
            desc:"La pleuritis es una inflamación de la pleura (la capa que cubre los pulmones) causada por una infección o una lesión. Los síntomas pueden incluir dolor en el pecho que se agrava al respirar profundamente, tos, fiebre y sudoración."
        },
    ]

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
div{
    width: 35%;
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