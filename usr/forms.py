__author__ = 'dreicon88'
# -*- encoding: utf8 -*-
from django import forms
from usr.models import Cliente,User

class ClienteForm(forms.Form):
    username = forms.CharField(label="*Nombre de Usuario", widget=forms.TextInput())
    email = forms.EmailField(label="*Correo Electronico", widget=forms.TextInput())
    nombre = forms.CharField(label="*Nombre", widget=forms.TextInput())
    apellidos = forms.CharField(label="*Apellidos", widget=forms.TextInput())
    password_one = forms.CharField(label="*Password", widget=forms.PasswordInput(render_value=False))
    password_two = forms.CharField(label="*Confirmar Password", widget=forms.PasswordInput(render_value=False))

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            u = User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('Este nombre de usuario ya existe')

    #end def

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            u = User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('Ya existe un usuario con este correo')
    #end def
    

    def clean_password_two(self):
        password_one = self.cleaned_data['password_one']
        password_two = self.cleaned_data['password_two']
        if password_one == password_two:
            pass
        else:
            raise forms.ValidationError('Las contraseñas no coinciden')
        #end if
    #end def
#end class

class ChangePasswordForm(forms.Form):
    username = forms.CharField(label="Username")
    mail = forms.EmailField(label="Email")
    newPassword1 = forms.CharField(label="Nueva Contraseña", widget=forms.PasswordInput(render_value=False))
    newPassword2 = forms.CharField(label="Vuelve a escribir la contraseña nueva",
                                   widget=forms.PasswordInput(render_value=False))

    def clean_user(self):
        username = self.cleaned_data['username']
        u = User.objects.filter(username=username)
        if len(u) == 0:
            raise forms.ValidationError('No existe un usuario con ese Username')
        return username
        #end if
    #end def

    def clean_mail(self):
        mail = self.cleaned_data['mail']
        u = User.objects.filter(email=mail)
        if len(u) == 0:
            raise forms.ValidationError('No existe un usuario con ese Email')
        return mail
        #end if
    #end def

    def clean_newPassword2(self):
        password1 = self.cleaned_data['newPassword1']
        password2 = self.cleaned_data['newPassword2']
        if password1 == password2:
            pass
        else:
            raise forms.ValidationError('Las contraseñas no coiciden')
        #end if
     #end def
#end class