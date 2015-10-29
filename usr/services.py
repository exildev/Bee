# -*- encoding: utf8 -*-
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from models import Desarrollador, Cliente
from forms import ClienteForm, ChangePasswordForm


class UsrService():
    instance = None

    @staticmethod
    def get_instance():
        if UsrService.instance == None:
            UsrService.instance = UsrService()
        #end if
        return UsrService.instance
    #end def

    def login(self,request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return True
            #end if
        #end if
        return False
     #end def

    def logout(self, request):
        logout(request)
        return True
    #end def

    def es_usuario(self, request):
        if request.user.is_authenticated():
            return True
        #end if
        return False
    #end def

    def es_cliente(self, request):
        if self.es_usuario(request):
            clientes = Cliente.objects.filter(usuario = request.user)[:1]
            if len(clientes):
                return clientes[0]
                #end f
        #end if
        return False
    #end def

    def es_desarrollador(self, request):
        if self.es_usuario(request):
            desarrolladors = Desarrollador.objects.filter(usuario = request.user)[:1]
            if len(desarrolladors):
                return desarrolladors[0]
                #end if
        #end if
        return False
    #end def

    def add_cliente(self,request):
        print request.POST
        if request.method == "POST" :
            form = ClienteForm(request.POST)
            if form.is_valid() :
                username = form.cleaned_data['username']
                password = form.cleaned_data['password_one']
                email = form.cleaned_data['email']
                u = User.objects.create_user(username=username, email=email,
                                             password=password)
                u.set_password(raw_password=password)
                u.is_active = True
                u.save()
                cli = Cliente(usuario=u)
                cli.save()
                return True,[username,password]
            #end if
            return False,form
        #end if
        return False,ClienteForm()
    #end def

    def pass_cambio(self,request):
        if request.method == "POST" :
            form = ChangePasswordForm(request.POST)
            if form.is_valid():
                email = request.POST.get('mail')
                password = request.POST.get('newPassword2')
                u = User.objects.get(email=email)
                u.set_password(raw_password=password)
                u.save()
                return True,None
            #end if
            return False,form
        #end if
        return False,ClienteForm()
    #end def


#end class