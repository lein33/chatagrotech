from django.urls import path,include

from . import views
app_name = 'recetagro'
urlpatterns = [
    path('', views.home.as_view(),name='home'),
    path('servicios', views.Servicios.as_view(),name='servicios'),

	path('test',views.whatsAppWebhook,name='whatsapp-webhook'),
    

]