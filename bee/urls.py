# -*- encoding: utf8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:  form/hacer/peticion/
    url(r'^$', 'bee.views.index', name='home'),
    url(r'^form/agregar/software/', 'bee.views.form_agregar_software'),
    url(r'^agregar/software/', 'bee.views.agregar_software'),
    url(r'^form/hacer/peticion/', 'bee.views.form_hacer_peticion'),
    url(r'^hacer/peticion/', 'bee.views.hacer_peticion'),
    url(r'^mostrar/peticion/(?P<peticion_id>\d+)/', 'bee.views.mostrar_peticion'),
    url(r'^mostrar/software/(?P<software_id>\d+)/', 'bee.views.mostrar_software'),
    url(r'^buscar/softwares/', 'bee.views.buscar_softwares', name="busq_soft"),
    url(r'^busqueda/guardada/', 'bee.views.busquedas_guardadas',name="busq_save"),
    url(r'^ws/solicitar/software/','bee.views.ws_realizar_solicitud',name="sol_soft"),
    url(r'^solicitar/software/','bee.views.solicitud_software',name="soli_soft"),
    url(r'^contacto/','bee.views.contacto',name="contacto"),
    url(r'^vista/desarrollador/','bee.views.desarrollador_vista'),
    url(r'^software/solicitados/','bee.views.softwaresolicitados',name='soft_requeridos'),
    url(r'^ws/software/solicitados/','bee.views.softrequerido',name='soft_requerido'),
    url(r'^vista/registrar/software/','bee.views.softpara_registrar',name='soft_para_registrar'),
    url(r'^software/desarrollador/','bee.views.software_desarrollador',name='software_desarrollador'),
    url(r'^clientes/solicitudes/','bee.views.cliente_solicitudes',name='cliente_solicitudes'),
    url(r'^desarrollar/solicitud/','bee.views.desarrollar_solicitud',name='des_solicitud'),
    url(r'^ws/load/peticiones/$','bee.views.load_peticiones',name='load_peticiones'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^usr/', include('usr.urls')),
)

urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
