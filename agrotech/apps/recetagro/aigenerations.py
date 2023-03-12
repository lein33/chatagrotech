import os
import openai
from django.conf import settings
openai.api_key = settings.OPENAI_API_KEY

def descripcion_general(tipo_industria):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="ayudame con una descripcion general de un informe agricola de un cultivo para la empresa {}".format(tipo_industria)
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
            return tipo_industria+answer
        else:
            return ''
    else:
        return ''
    


def servicios(tipo_industria,servicios):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Describe varios servicios que la industria {} empleando {} los servicios gana mercado".format(tipo_industria,servicios),
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
            return tipo_industria+answer
        else:
            return ''
    else:
        return ''
    
def servicio_uno(tipo_industria,servicios):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="describe en 30 palabras en que consiste un asesoramiento {} de la empresa {}".format(tipo_industria,servicios),
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
            return tipo_industria+answer
        else:
            return ''
    else:
        return ''
def servicio_dos(tipo_industria,servicios):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="describe en 30 palabras en que consiste un {} de la empresa {}".format(servicios,tipo_industria),
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
            return tipo_industria+answer
        else:
            return ''
    else:
        return ''

def servicio_tres(tipo_industria,servicios):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="describe en 30 palabras en que consiste {} de la empresa {}".format(servicios, tipo_industria),
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
            return tipo_industria+answer
        else:
            return ''
    else:
        return ''



def razones(tipo_industria,servicios,tamaño_industria):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Describe en 50 palabras la Razon que justifique el uso de los productos {} sabiendo que el servicio mas atractivo es {} si su tamaño es {}".format(tipo_industria,servicios,tamaño_industria),
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
            return tipo_industria+answer
        else:
            return ''
    else:
        return ''
    
def comentario(tipo_industria,tamaño_industria):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="que argumentos deberia responder si manifiestan que los {} son muy necesarios si la empresa es {}".format(tipo_industria,tamaño_industria),
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
            return tipo_industria+answer
        else:
            return ''
    else:
        return ''
    
