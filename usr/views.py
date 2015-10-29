# -*- encoding: utf8 -*-
from django.shortcuts import render, redirect
from services import UsrService
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def login(request):
	error = request.GET.get('error', '')
	return render(request, 'usr/login.html', {'error':error})
#end def

def login_do(request):
	usr = UsrService.get_instance()
	if usr.login(request):
		return HttpResponse(status=200)
	#end if
	return HttpResponse(status=400)
#end def

def logout(request):
	usr = UsrService.get_instance()
	usr.logout(request)
	return redirect("/")
#end def

@csrf_exempt
def pass_cambio(request):
    usr = UsrService.get_instance()
    r,f = usr.pass_cambio(request)
    if r :
        return HttpResponse('[{"r":true}]',content_type='application/json')
    #end if
    return render(request,'usr/pass_cambio.html',{'form':f})
#end def

@csrf_exempt
def add_cliente(request):
    usr = UsrService.get_instance()
    res,form = usr.add_cliente(request)
    if res :
        return HttpResponse('[{"r":true,"n":"%s","c":"%s"}]'%(form[0],form[1]),content_type='application/json')
    #end if
    return render(request,'usr/add_cliente.html',{'form':form})
#end def

