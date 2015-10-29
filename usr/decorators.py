# -*- encoding: utf8 -*-
from django.shortcuts import redirect
from services import UsrService

def cliente(view):
    def func(request, *args, **kwargs):
        usr = UsrService.get_instance()
        if usr.es_cliente(request):
            return view(request, *args, **kwargs)
        else:
            return redirect("/")
        #end if
    #end def
    return func
#end def

def desarrollador(view):
    def func(request, *args, **kwargs):
        usr = UsrService.get_instance()
        if usr.es_desarrollador(request):
            return view(request, *args, **kwargs)
        else:
            return redirect("/")
        #end if
    #end def
    return func
#end def


def usuario(view):
    def func(request, *args, **kwargs):
        usr = UsrService.get_instance()
        if usr.es_usuario(request):
            return view(request, *args, **kwargs)
        else:
            return redirect("/")
        #end if
    #end def
    return func
#end def