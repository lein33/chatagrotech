from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse

import json

from django.http import HttpResponse

from django.template.loader import get_template
import os
# Create your views here.
def home(request):
    return render(request,'index.html',{})