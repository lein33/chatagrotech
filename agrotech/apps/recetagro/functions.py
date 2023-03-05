from django.conf import settings
import requests
import json
from .models import *
from django.http import HttpResponse
from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render

import pdfkit
from django.template.loader import get_template
#from .aigenerations import *
import os
from threading import Thread

class CustomThread(Thread):
    def __init__(self,group=None,target=None,name=None,args=(),kwargs={},Verbose=None):
        Thread.__init__(self,group,target,name,args,kwargs)
        self.__return = None
    
    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args,**self._kwargs)

    def join(self):
        Thread.join(self)
        return self._return
        
def sendWhatsAppMessage(phoneNumber, message):
    headers = {"Authorization": settings.WHATSAPP_TOKEN}
    payload = {
        "messaging_product":"whatsapp",
        "recipient_type":"individual",
        "to":phoneNumber,
        "type":"text",
        "text":{
            "body":message
        }
    }
    response = requests.post(settings.WHATSAPP_URL,headers=headers,json=payload)
    ans = response.json()
    return ans

def handleWhatsAppChat(fromId, profileName, phoneId,text):
    try:
        chat = ChatSessions.objects.get(perfil__phoneNumber=fromId)
    except:
        if User.objects.filter(username=phoneId).exists():
            usuario = User.objects.get(username=phoneId)
            user_profile = usuario.profile
        
        else:
            usuario = User.objects.create_user(
            username=phoneId,
            email='te3ster@gfkfm-tech',
            password='04.desnutryfy',
            first_name=profileName)

            user_profile = Perfil.objects.create(
            user=usuario,
            phoneNumber=fromId,
            phoneId=phoneId)
            
        chat = ChatSessions.objects.create(perfil=user_profile)
        message ="Bienvenido al asistente EL Plan estrategico Empresarial 🧔‍♂️🧔👩‍🦳🌰"
        sendWhatsAppMessage(fromId,message)
    
    if chat.tipo_industria:
        if chat.tipo_servicio:
            pass
        else:
            chat.tipo_servicio='pequeña'
            chat.save()
            message="Que tamaño necesitas"
            sendWhatsAppMessage(fromId,message)