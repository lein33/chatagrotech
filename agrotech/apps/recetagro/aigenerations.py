import os
import openai
from django.conf import settings
openai.api_key = settings.OPENAI_API_KEY

def descripcion_general(tipo_industria,tamaño_industria):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="una descripcion general de un informe {} para cultivos ".format(tipo_industria),
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
    
    
def servicio_uno(tipo_industria):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="describe el analisis de suelo para un cultivo {} en 40 palabras".format(tipo_industria),
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
def servicio_dos(tipo_industria):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="describe practicas de un cultivo {} en 40 palabras".format(tipo_industria),
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

def servicio_tres(tipo_industria):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="describe la proteccion de un cultivo {} en 40 palabras".format(tipo_industria),
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



def razones(tipo_industria):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="razones para diseñar un informe tecnico {}".format(tipo_industria),
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
    
