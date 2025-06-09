from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User 
from .models import Contrasenia


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form_usuario',
            'placeholder':'Nombre de Usuario'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class':'form_usuario',
            'placeholder': 'Contraseña'
        })
    )

class RegistroForm(UserCreationForm):
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'form_usuario',
            'placeholder': 'Contraseña'
        })
    )
    password2 = forms.CharField(
        label="Confirmar Contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'form_usuario',
            'placeholder': 'Confirmar Contraseña'
        })
    )
    
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form_usuario', 'placeholder':'Nombre de Usuario'}),
        }

class ContraseniaForm(forms.ModelForm):
    class Meta: 
        model = Contrasenia 
        fields = ['servicio', 'email', 'usuario_servicio', 'contrasenia']
        widgets = {
            'servicio': forms.TextInput(attrs={'class': 'form_contrasenia', 'placeholder':'Nombre del Servicio'}),
            'email': forms.EmailInput(attrs={'class': 'form_contrasenia', 'placeholder':'Email'}),
            'usuario_servicio': forms.TextInput(attrs={'class': 'form_contrasenia', 'placeholder':'Nombre de Usuario'}),
            'contrasenia': forms.TextInput(attrs={'class': 'form_contrasenia', 'placeholder':'Contraseña'}),
        }