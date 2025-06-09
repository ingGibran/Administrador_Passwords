from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout 
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm, ContraseniaForm, CustomLoginForm
from .models import Contrasenia

# Create your views here.
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid() :
            user = form.save()
            login(request, user)
            return redirect('administrador')
    else:
        form = RegistroForm()
    return render(request, 'administrador/registro.html', {'form':form})

def iniciar_sesion(request):
    if request.method == 'POST':
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('administrador')
    else:
        form = CustomLoginForm()
    
    return render(request, 'administrador/inicio_sesion.html', {'form':form})

@login_required
def administrador(request):
    if request.method == 'POST':
        form = ContraseniaForm(request.POST)
        if form.is_valid():
            contrasenia = form.save(commit=False)
            contrasenia.usuario = request.user
            contrasenia.save()
            return redirect('administrador')
    else:
        form = ContraseniaForm()
    
    contrasenias = Contrasenia.objects.filter(usuario=request.user)
    return render(request, 'administrador/admin.html', {'form':form,'contrasenias':contrasenias})

@login_required 
def editar(request, pk):
    contrasenia = get_object_or_404(Contrasenia, pk=pk)
    
    if request.method == 'POST':
        form = ContraseniaForm(request.POST, instance=contrasenia)
        if form.is_valid():
            form.save()
            return redirect('administracion')
    else:
        form = ContraseniaForm()
        
    return render(request, 'administrador/editar_contrasenia.html', {
        'form':form,
        'contrasenia':contrasenia
    })