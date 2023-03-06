from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone
from uuid import uuid4
from django.conf import settings
import os

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneNumber = models.CharField(null=True, blank=True,max_length=100)
    phoneId = models.CharField(null=True, blank=True,max_length=100)
    
    uniqueId = models.CharField(null=True, blank=True,unique=True,max_length=100)
    fecha_creacion = models.DateTimeField(blank=True,null=True)
    ultima_edicion = models.DateTimeField(blank=True,null=True)

    def save(self, *args, **kwargs):
        if self.fecha_creacion is None:
            self.fecha_creacion = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
        
        self.ultima_edicion = timezone.localtime(timezone.now())
        super(Perfil, self).save(*args,**kwargs)

class About(models.Model):
    perfil = models.ForeignKey(Perfil,on_delete=models.CASCADE,null=True,blank=True)
    descripcion_general = models.TextField(null=True, blank=True)
    servicios = models.TextField(null=True, blank=True)
    razones = models.TextField(null=True, blank=True)
    comentario = models.TextField(null=True, blank=True)

    uniqueId = models.CharField(null=True,blank=True,unique=True,max_length=100)
    fecha_creacion = models.DateTimeField(blank=True,null=True)
    ultima_edicion = models.DateTimeField(blank=True,null=True)
    
    def __str__(self):
        return self.perfil.user
    def save(self,*args,**kwargs):
        if self.fecha_creacion is None:
            self.fecha_creacion = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
        
        self.ultima_edicion = timezone.localtime(timezone.now())
        super(About, self).save(*args,**kwargs)


class ChatSessions(models.Model):
    opciones=[
        ('1','pequeña'),
        ('2','media'),
        ('3','grande'),
    ]
    tipo_industria = models.TextField(null=True, blank=True)
    tipo_servicio = models.TextField(null=True, blank=True)
    tamaño_industria = models.TextField(choices=opciones, null=True, blank=True)
    comentario = models.TextField(null=True, blank=True)
    
    
    perfil = models.ForeignKey(Perfil,on_delete=models.CASCADE,null=True,blank=True)
   
    uniqueId = models.CharField(null=True,blank=True,unique=True,max_length=100)
    fecha_creacion = models.DateTimeField(blank=True,null=True)
    ultima_edicion = models.DateTimeField(blank=True,null=True)
    
    def save(self,*args,**kwargs):
        if self.fecha_creacion is None:
            self.fecha_creacion = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
        
        self.ultima_edicion = timezone.localtime(timezone.now())
        super(ChatSessions, self).save(*args,**kwargs)
