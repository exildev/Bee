# -*- encoding: utf8 -*-
from django.contrib import admin
from models import Verbo, Complemento, Horacion, Peticion, Requerimiento, Software, Vista_requerimiento, Vista_peticion,Solicitud,SofwareRequerido,Contacta,Desarrollos

admin.site.register(Verbo)
admin.site.register(Complemento)
admin.site.register(Horacion)
admin.site.register(Peticion)
admin.site.register(Requerimiento)
admin.site.register(Software)
admin.site.register(Vista_requerimiento)
admin.site.register(Vista_peticion)
admin.site.register(Solicitud)
admin.site.register(SofwareRequerido)
admin.site.register(Contacta)
admin.site.register(Desarrollos)