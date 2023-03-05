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