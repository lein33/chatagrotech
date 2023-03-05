from django.urls import path,include
from apps.recetagro.views import *

urlpatterns = [
    path('', home,name='home'),
	#path('test',views.whatsAppWebhook,name='whatsapp-webhook'),
    

]