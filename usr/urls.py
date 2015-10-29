# -*- encoding: utf8 -*-
from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    url(r'^login/$', 'usr.views.login'),
    url(r'^login/do/$', 'usr.views.login_do'),
    url(r'^logout/$', 'usr.views.logout'),
    url(r'^pass/cambio/$','usr.views.pass_cambio',name='pass_cambio'),
    url(r'^add/cliente/$','usr.views.add_cliente',name='add_cliente')

)
