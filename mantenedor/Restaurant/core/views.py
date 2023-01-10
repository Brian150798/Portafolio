from django.shortcuts import render, redirect
from .models import Plato
from core.forms import PlatoForm
# Create your views here.
def home(request):
    platos = Plato.objects.all()
    contexto = {
        'platos':platos
    }
    return render(request,'core/home.html', contexto)

def form_plato(request):
    formulario = PlatoForm()
    
    contexto = {
        'form':PlatoForm()
    }
    if request.method == 'POST':
        formulario = PlatoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            contexto['mensaje'] = "Guardado Correctamente"
    return render(request,'core/form_plato.html', contexto)

def form_mod_plato(request,id):
    plato = Plato.objects.get(idPlato = id)

    contexto = {
        'form' : PlatoForm(instance=plato)
    }

    if request.method == 'POST':
        formulario = PlatoForm(data=request.POST,instance=plato)
        if formulario.is_valid:
            formulario.save()
            contexto['mensaje'] = "Modificado Correctamente"


    return render (request, 'core/form_mod_plato.html',contexto)

def form_del_plato(request,id):
    plato = Plato.objects.get(idPlato = id)

    plato.delete()

    return redirect (to="home")
