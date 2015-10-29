# -*- encoding: utf8 -*-
from django.db.models import F
from models import Peticion, Horacion, Complemento, Verbo, Vista_requerimiento, Vista_peticion, Software, Requerimiento,Solicitud,SofwareRequerido,Contacta
from apicultur import apicultur_post, endhs
from forms import SoftwareForm,SoftwareFormTem
from datetime import datetime
from django.db import connection
from forms import SoftwareRequeridoForm,ContactaForm,SoftwareRequeridoForm2
import json as simplejson
from usr.models import Desarrollador



class BeeService():
    instance = None

    @staticmethod
    def get_instance():
        if BeeService.instance == None:
            BeeService.instance = BeeService()
        #end if
        return BeeService.instance
    #end def

    def hacer_peticion(self, request):
        texto = request.POST.get('texto', False)
        if texto:
            horaciones = self.apicultur(texto)
            peticion = Peticion(fecha=datetime.now(), texto=texto,usuario=request.user,tipo=0)
            peticion.save()
            for horacion in horaciones:
                peticion.horaciones.add(horacion)
            #end for
            return peticion
        #end if
        return False
    #end def

    def agregar_software(self, request):
        descripcion = request.POST.get('descripcion', False)
        print descripcion
        print request.POST
        form = SoftwareForm(request.POST, files=request.FILES)
        if form.is_valid():
            software = form.save(commit=False)
            software.puntos = 0
            software.numero = 0
            software.desarrollador= request.user
            horaciones = self.apicultur(descripcion)
            software.save()
            for horacion in horaciones:
                requerimiento = Requerimiento(descripcion=horacion.texto)
                requerimiento.save()
                requerimiento.horaciones.add(horacion)
                software.requerimientos.add(requerimiento)
            #end for
            return software
        #end if
        form = SoftwareFormTem(request.POST, files=request.FILES)
        form.is_valid()
        return False,form
    #end def

    def apicultur(self, texto):
        json = apicultur_post(texto)
        horaciones = []
        complementos = []
        texto = ''
        verbos = []
        for palabra in json:
            categoria = palabra['lemas'][0]['categoria']
            lema = palabra['lemas'][0]['lema']
            simple = palabra['palabra']
            print categoria, lema
            if categoria.startswith('VM'):
                verbos.append({'nombre':lema, 'codigo':categoria})
            elif categoria.startswith('NC') or categoria.startswith('AQ') or categoria in ['Z', 'NP00000']:
                complementos.append({'nombre':lema, 'codigo':categoria})
            elif categoria in endhs:
                for verbo in verbos:
                    if verbo and len(complementos):
                        verb, created = Verbo.objects.get_or_create(nombre=verbo['nombre'], codigo=verbo['codigo'])
                        horacion = Horacion(verbo = verb, texto = texto)
                        horacion.save()
                        for comp in complementos:
                            complemento, created = Complemento.objects.get_or_create(nombre=comp['nombre'])
                            Complemento.objects.filter(pk = complemento.pk).update(codigo=comp['codigo'])
                            horacion.complementos.add(complemento)
                        #end for
                        horaciones.append(horacion)
                        texto = ''
                    #end if
                #end for
                complementos = []
                verbos=[]
            #end if
            texto += ' ' + simple
            print verbos,'**',complementos
        #end for
        return horaciones
    #end if

    def mostrar_peticion(self, request, peticion_id):
        peticiones = Peticion.objects.filter(id = peticion_id)
        if len(peticiones):
            peticion = peticiones[0]
            keywords = Vista_peticion.objects.filter(peticion = peticion).values('keyword')
            requerimientos = Vista_requerimiento.objects.filter(keyword__in = keywords)
            return {'peticion':peticion, 'requerimientos': requerimientos}
        #end if
        return None
    #end def

    def buscar_softwares(self, request):
        requerimientos = request.POST.getlist('requerimientos')
        cursor = connection.cursor()
        cursor.execute('select get_software_cons_cli(%d,\'%s\')'%(request.user.id,'{%s}'%(','.join(map(str,requerimientos)))))
        row = cursor.fetchone()
        return Software.objects.filter(requerimientos__pk__in = requerimientos).order_by('-puntos'),simplejson.loads('%s'%row[0])
    #end def

    

    def mostrar_software(self, request, pk):
        softwares = Software.objects.filter(pk = pk)
        if len(softwares):
            softwares.update(puntos = F('puntos') + 1)
            return softwares[0]
        #end def
        return False
    #end def

    def busquedas_guardadas(self,request):
        cursor = connection.cursor()
        cursor.execute('select software_solicitados_cliente(%d)'%request.user.id)
        row = cursor.fetchone()
        return simplejson.loads('%s'%row[0])
    #end def

    def software_solicitados(self,request):
        cursor = connection.cursor()
        print "Los solicito aqui jajajjaja   ",request.user.id
        cursor.execute('select get_solicitudes(%d)'%request.user.id)
        row = cursor.fetchone()
        return simplejson.loads('%s'%row[0])
    #end def

    def realizar_solicitud(self,request):
        if request.POST.get('s',False) :
            s = Software.objects.filter(id=int(request.POST.get('s'))).first()
            if s :
                sol = Solicitud.objects.filter(cliente=request.user,software=s).first()
                if sol :
                    return "false"
                #end fi
                so = Solicitud(cliente=request.user,software=s)
                so.save()
                return "true"
            #end if
            return "false"
        #end if
        return "false"
    #end def

    def sofware_medida(self,request):
        form = SoftwareRequeridoForm(request.POST)
        texto = request.POST.get("descripcion", False)
        if form.is_valid() and texto:
            add = form.save(commit=False)
            ora = self.apicultur(texto)
            sr  = SofwareRequerido(descripcion = add.descripcion, cliente = request.user)
            sr.save()
            for oracion in ora:
                sr.oraciones.add(oracion)
            #end for
            return True
        #end if
        return form
    #end def

    def contactanos(self,request):
        form = ContactaForm(request.POST)
        if form.is_valid():
            add=form.save(commit=False)
            c = Contacta(descripcion=add.descripcion,cliente=request.user)
            c.save()
            return  True
        #end if
        return form
    #end def

    def softrequerido(self,request):
        re = request.POST.get('r',False)
        if re :
            r = Solicitud.objects.filter(id=re).first()
            if r :
                if r.estado :
                    r.estado=False
                else:
                    r.estado=True
                #end if
                r.save()
            #end if
            print r.estado
            return "true"
        #end def
        return 'false'
    #end def

    def software_desarrollador(self,request):
        return Software.objects.filter(desarrollador=request.user)
    #end def

    def desarrollar_solicitud(self,request):
        if request.POST.get('id',False):
            s = SofwareRequerido.objects.filter(id=int(request.POST.get('id'))).first()
            if s :
                d = Desarrollador.objects.filter(usuario=request.user).first()
                if d :
                    s.desarrollador=d
                    s.estado=True
                    s.save()
                    return "true"
                #end if
            #end if
        #end if
        return "false"
    #end def

    def load_peticiones(self,request):
        print request.GET
        length=request.GET.get('length')
        order = request.GET.get('order[0][dir]',0)
        start  = request.GET.get('start',0)
        search = request.GET.get('search[value]',False)
        print length,order,start,search
        cursor = connection.cursor()
        cursor.execute(' select * from new_sof_sol_des4(%d,\'%s\',%s::integer,%s::integer,%s::integer)'%(request.user.id,search if search else "",1,start,length)) 
        row =cursor.fetchone()
        """
        print len(simplejson.loads('%s'%row[0]))," Tamaño "
        d = {'recordsTotal':len(self.softwaresolicitados(request)), 'recordsFiltered':len(simplejson.loads('%s'%row[0])), 'data':row[0]}
        l = list()
        l.append(d)
        print l
        """
        print type(row[0])
        print row[0].replace("qwerty","data")
        c = ((row[0].replace("qwerty","data")).replace("recordstotal","recordsTotal")).replace("recordsfiltered","recordsFiltered")
        return '%s'%c[1:len(c)-1]
    #end def

    def softwaresolicitados(self,request):
        print "id del user ",request.user.id
        cursor = connection.cursor()
        print request.user.id
        cursor.execute('select sof_sol_des(%d)'%request.user.id)
        row = cursor.fetchone()
        return simplejson.loads('%s'%row[0])
    #end def

#end class
