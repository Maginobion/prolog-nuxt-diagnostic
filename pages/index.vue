<template>
    <main>
        <h1>Diagnóstico online</h1>
        <form @submit.prevent="consultar">
            <div class="radioGrid">
                <QuestionRadio
                    v-for="(question,index) in questions"
                    :key="question"
                    :question-name="question"
                    :id="(index+1).toString()"
                />
            </div>
            <input type="submit" value="Enviar"/>
        </form>
    </main>
</template>

<script setup lang="ts">

    definePageMeta({
        pageTransition: {
            name: 'slide-right',
            mode: 'out-in'
        },
    })

    const consultar = async (e:Event) =>{
        const inputs = e.target as HTMLFormElement
        const formData = new FormData(inputs)
        const formProps = Object.fromEntries(formData) as { [a: string]: string | number }
        console.log(formProps)
        await $fetch('/api/consultaProlog',{
            method:'post',
            body: formProps
        })
        .then(res=>{
            res.status && res.stdout ? navigate(res.stdout) : navigateTo('/result')
        })
    }

    const navigate = (val:string) =>{
        navigateTo({
            path:'result',
            query:{
                disease: val
            }
        })
    }

    const questions = [
        "Dolor en el pecho",
        "Fiebre alta",
        "Sudoración nocturna",
        "Cansancio extremo",
        "Perdida de apetito",
        "Perdida de peso",
        "Fiebre baja",
        "Fatiga",
        "Dolor de cabeza",
        "Escalofrios",
        "Dolor abdominal",
        "Tos mas de 3 meses",
        "Tos con flema",
        "Dificultad para respirar",
        "Sudoración",
        "Tos cronica",
        "Perdida de peso",
        "Dolor en las articulaciones",
        "Sensación de presión en el pecho",
        "Tos norma",
    ]

</script>

<style scoped>
h1{
    color: #06b396;
}
main{
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
input{
    background-color: #F1064A;
    color: white;
    padding: 8px 18px;
    border: 0;
    font-size: large;
    border-radius: 4px;
    margin: auto;
}
.radioGrid{
    display: grid;
    grid-template-columns: repeat(4,1fr);
    gap: 2rem;
    margin-bottom: 1rem;
}
form{
    display: flex;
    flex-direction: column;
    gap: 14px;
    margin: 2rem;
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