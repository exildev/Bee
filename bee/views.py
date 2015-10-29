# -*- encoding: utf8 -*-
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from services import BeeService
from usr.services import UsrService
from usr.decorators import cliente, desarrollador
from django.views.decorators.csrf import csrf_exempt
from forms import SoftwareRequeridoForm,ContactaForm

def index(request):
    usr = UsrService.get_instance()
    print "Llegando aqui jaja",usr.es_cliente(request),request.user.username
    if usr.es_desarrollador(request):
        print "1"
        return redirect("/vista/desarrollador/")
    elif usr.es_cliente(request):
        print "2"
        return redirect("/form/hacer/peticion/")
    else:
        print "3"
        return redirect("/usr/login/")
    #end if
#end def

@cliente
def form_hacer_peticion(request):
    return render(request, 'hacer_peticion.html')
#end def


@cliente
def hacer_peticion(request):
    bee = BeeService.get_instance()
    peticion = bee.hacer_peticion(request)
    if peticion:
        return redirect('/mostrar/peticion/' + str(peticion.pk) + '/')
    #end if
    return HttpResponse('error')
#end def

@desarrollador
def form_agregar_software(request):
    return render(request, 'agregar_software.html')
#end def

@desarrollador
def desarrollador_vista(request):
    return render(request,'desarrollador2.html')
#end def

@csrf_exempt
@desarrollador
def softwaresolicitados(request):
    bee = BeeService.get_instance()
    s = bee.softwaresolicitados(request)
    return render(request,'pedidos.html',{'s':s})
#end def

@desarrollador
def agregar_software(request):
    bee = BeeService.get_instance()
    software = bee.agregar_software(request)
    if software:
        return HttpResponse('true')#return redirect('/mostrar/software/' + str(software.pk) + '/')
    #end if
    return HttpResponse(software[0])
#end def

@cliente
def mostrar_peticion(request, peticion_id):
    bee = BeeService.get_instance()
    peticion = bee.mostrar_peticion(request, peticion_id)
    if peticion:
        return render(request, 'mostrar_peticion.html', {'peticion':peticion})
    #end if
    return HttpResponse('error')
#end def

@cliente
def buscar_softwares(request):
    bee = BeeService.get_instance()
    softwares = bee.buscar_softwares(request)
    return render(request, 'buscar_softwares.html', {'softwares':softwares[0],'peticion':request.POST.get('p'),'s':softwares[1]})
#end def

@cliente
def mostrar_software(request, software_id):
    bee = BeeService.get_instance()
    software = bee.mostrar_software(request, software_id)
    if software:
        return render(request, 'mostrar_software.html', {'software':software})
    #end if
    return HttpResponse('error')
#end def

@cliente
def busquedas_guardadas(request):
    bee = BeeService.get_instance()
    softwares = bee.busquedas_guardadas(request)
    return render(request, 'buscar_softwares.html', {'s':softwares})
#end def

@csrf_exempt
def ws_realizar_solicitud(request):
    bee = BeeService.get_instance()
    return HttpResponse('[{"r":%s}]'%(bee.realizar_solicitud(request)),content_type='application/json')
#end def

@csrf_exempt
@cliente
def solicitud_software(request):
    if request.POST:
        bee = BeeService.get_instance()
        b = bee.sofware_medida(request)
        if b:
            return render(request,'software_medida.html',{'form':SoftwareRequeridoForm()})
        #end if
        return render(request,'software_medida.html',{'form':b})
    #end if
    return render(request,'software_medida.html',{'form':SoftwareRequeridoForm()})
#end def

@csrf_exempt
@cliente
def contacto(request):
    if request.POST :
        bee = BeeService.get_instance()
        d=bee.contactanos(request)
        if d :
            return render(request,'contactenos.html',{'form':ContactaForm()})
        #end if
        return render(request,'contactenos.html',{'form':d})
    #end if
    return render(request,'contactenos.html',{'form':ContactaForm()})
#end def

@csrf_exempt
@desarrollador
def softrequerido(request):
    bee = BeeService.get_instance()
    d=bee.softrequerido(request)
    return HttpResponse('[{"r":%s}]'%d,content_type='application/json')
#end def

@desarrollador
def softpara_registrar(request):
    return render(request,'registro_software.html',{})
#end def

@desarrollador
def software_desarrollador(request):
	bee = BeeService.get_instance()
	return render(request,'softdesarrollador.html',{'software':bee.software_desarrollador(request)})
#end def

@desarrollador
def cliente_solicitudes(request):
    bee = BeeService.get_instance()
    print ':::::::::::::::::'
    return render(request,'lista_peticiones_software.html',{'s':bee.software_solicitados(request)})
#end def

@csrf_exempt
@desarrollador
def desarrollar_solicitud(request):
    bee = BeeService.get_instance()
    return HttpResponse('[{"r":%s}]'%bee.desarrollar_solicitud(request),content_type='application/json')
#end def

@csrf_exempt
@desarrollador
def load_peticiones(request):
    bee = BeeService.get_instance()
    return HttpResponse(bee.load_peticiones(request),content_type='application/json')
#end def