import os
import openai
from django.conf import settings
openai.api_key = settings.OPENAI_API_KEY

def descripcion_general(tipo_industria,tamaño_empresa):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Describe un resumen de las actividades que realiza la industria {} considerando su tamaño {} \n\n".format(tipo_industria,tamaño_empresa),
        temperature=0.33,
        max_tokens=2000,
        top_p=1,
        best_of=2,
        frequency_penalty=0,
        presence_penalty=0
    )

    if 'choices' in response:
        if len(response['choices'])>0:
            answer = response['choices'][0]['text'].replace('\n','\n')
            return nombre_empresa+answer
        else:
            return ''
    else:
        return ''
    
