import { exec } from 'child-process-promise'

export default defineEventHandler(async (event)=>{

    const test = await readBody(event)

    const values = Object.values(test)

    // let validText = ''

    // values.forEach((val)=>{
    //     validText+="'"+val+"',"
    // })

    // const slicing = validText.slice(0,validText.length-1)

    // console.log(slicing)

    const archivo = "diagnostico.pl"
    // const command = 'swipl -s '+archivo+' -g "test('+values+')." -t halt.'
    const cmd = `swipl -s ${archivo} -g "test([${values}])" -t halt`

    let output,status

    await exec(cmd)
    .then(out=>{
        output=out.stdout
        status=true
    })
    .catch(err=>{
        output=err.stderr
        status=false
    })

    console.log('Salida ', output)

    return{
        stdout: output,
        status: status
    }
})