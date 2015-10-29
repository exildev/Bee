# -*- encoding: utf8 -*-
from django import forms
from models import Software, Requerimiento,SofwareRequerido,Contacta
from django.contrib.auth.models import User

class SoftwareForm(forms.ModelForm):
	nombre = forms.CharField(max_length=45)
	requerimientos = forms.ModelMultipleChoiceField(queryset=Requerimiento.objects,required=False)
	descripcion = forms.Textarea()
	puntos = forms.IntegerField(required=False)
	numero = forms.IntegerField(required=False)
	imagen = forms.ImageField()
	class Meta:
		model = Software
		exclude=()
	#end class
#end class

class SoftwareFormTem(forms.ModelForm):
	class Meta :
		model= Software
		exclude=('requerimientos','puntos','numero')
	#end class
#end class

class SoftwareRequeridoForm(forms.ModelForm):

	class Meta :
		model = SofwareRequerido
		exclude = ('cliente','desarrollador','estado', 'oraciones')
	#end class
#end class

class SoftwareRequeridoForm2(forms.ModelForm):

	class Meta :
		model = SofwareRequerido
		exclude = ('desarrollador','estado')
	#end class
#end class

class ContactaForm(forms.ModelForm):

	class Meta :
		model = Contacta
		exclude = ('cliente','estado')
	#end class
#end class

