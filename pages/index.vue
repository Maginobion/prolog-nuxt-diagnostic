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

    const output = ref('')

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

    const enfermedades = [

    ]

    const questions = [
        "Dolor de espalda",
        "Dolor de dientes",
        "Caída del cabello",
        "Mareos",
        "Elpepe",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
        "18",
        "19",
        "20"
    ]

</script>

<style scoped>
h1{
    color: #00B295;
}
main{
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