# -*- encoding: utf8 -*-
from django.contrib.auth.models import User
from django.db import models
from usr.models import Cliente,Desarrollador


class Verbo(models.Model):
    nombre = models.CharField(max_length=45)
    codigo = models.CharField(max_length=45)
    def __unicode__(self):
        return self.nombre
    #end def
#end class

class Complemento(models.Model):
    nombre = models.CharField(max_length=45)
    codigo = models.CharField(max_length=45, null=True)
    def __unicode__(self):
        return self.nombre
    #end def
#end class


class Horacion(models.Model):
    verbo = models.ForeignKey(Verbo)
    complementos = models.ManyToManyField(Complemento)
    texto = models.TextField()

    def __unicode__(self):
        return self.texto
    #end def
#end class

class Peticion(models.Model):
    Choice = ((0,'Consulta'),(1,'Medida'))
    tipo = models.IntegerField(choices=Choice)
    usuario = models.ForeignKey(User)
    horaciones = models.ManyToManyField(Horacion)
    fecha = models.DateTimeField()
    texto = models.TextField()
    def __unicode__(self):
        return self.texto
    #end def
#end class

class Requerimiento(models.Model):
    horaciones = models.ManyToManyField(Horacion)
    descripcion = models.TextField()
    def __unicode__(self):
        return self.descripcion
    #end def
#end class

class SofwareRequerido(models.Model):
    cliente = models.ForeignKey(User)
    descripcion = models.TextField()
    desarrollador = models.ForeignKey(Desarrollador,null=True,blank=True)
    estado = models.BooleanField(default=False)
    oraciones = models.ManyToManyField(Horacion)

    def  __unicode__(self):
        return self.cliente.username
    #end def
#end class

class Contacta(models.Model):
    cliente=models.ForeignKey(User)
    descripcion = models.TextField()
    estado = models.BooleanField(default=False)

    def __unicode__(self):
        return self.usuario.username
    #end def
#end def

class Software(models.Model):
    desarrollador = models.ForeignKey(User,null=True,blank=True)
    nombre = models.CharField(max_length=45)
    requerimientos = models.ManyToManyField(Requerimiento)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='logos')
    puntos = models.IntegerField()
    numero = models.IntegerField()

    def get_ranking(self):
        if self.numero != 0:
            return self.puntos / self.numero
        #end if
        return 3
    #end def

    def __unicode__(self):
        return self.nombre
    #end def
#end class

class Desarrollos(models.Model):
    desarrollador = models.ForeignKey(User)
    softwares = models.ManyToManyField(Software)

    def __unicode__(self):
        return self.desarrollador.username
    #end def
#end class


class Solicitud(models.Model):
    cliente = models.ForeignKey(User)
    software = models.ForeignKey(Software)
    estado = models.BooleanField(default=False)

    def __unicode__(self):
        return self.cliente.username
    #end def
#end class

class Vista_requerimiento(models.Model):
    descripcion = models.TextField()
    verbo = models.ForeignKey(Verbo)
    complemento = models.ForeignKey(Complemento)
    requerimiento = models.ForeignKey(Requerimiento)
    keyword = models.CharField(max_length=45)

    class Meta:
        db_table = 'vista_requerimiento'
    #end class

    def __unicode__(self):
        return self.descripcion
    #end def
#end class

class Vista_peticion(models.Model):
    texto = models.TextField()
    verbo = models.ForeignKey(Verbo)
    peticion = models.ForeignKey(Peticion)
    complemento = models.ForeignKey(Complemento)
    keyword = models.CharField(max_length=45)

    class Meta:
        db_table = 'vista_peticion'
    #end class

    def __unicode__(self):
        return self.texto
    #end def
#end class
