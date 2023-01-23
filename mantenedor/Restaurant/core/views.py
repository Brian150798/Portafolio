from django.shortcuts import render, redirect
from .models import Plato, Reservacion, Hora, Fecha, Bodega, Estado, Pedido, Receta, Mesa
from core.forms import PlatoForm, ReservacionForm, BodegaForm, CustomUserCreationForm, PedidoForm, CocinaForm, RecetaForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate,login

from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def registroUsuario(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            messages.success(request, "Usuario creado correctamente!")
            return render(request,'core/inicio.html')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registroUsuario.html',data)
    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username =form.cleaned_data['username']
    #         password =form.cleaned_data['password']
    #         user = authenticate(username=username, password=password)
    #         login(request, user)
    #         messages.success(request, 'Registro completado exitosamente!')
    #         return render(request,'core/inicio.html')
    # else:
    #     form = UserCreationForm()
    # return render(request, 'registration/registroUsuario.html', {'form':form})



def loogin(request):
    return redirect(request, 'registration/login.html')

def logout(request):
    logout(request)
    return redirect(request,'core/inicio.html')

def inicio(request):
    return render(request,'core/inicio.html')

def menu(request):
    platos = Plato.objects.all()
    contexto = {
        'platos':platos
    }
    return render(request, 'core/menu.html', contexto)

def mesa(request):
    mesas = Mesa.objects.all()
    contexto = {
        'mesas':mesas
    }
    return render(request, 'core/mesa.html', contexto)

def receta(request):
    recetas = Receta.objects.all()
    contexto = {
        'recetas':recetas
    }
    return render(request, 'core/receta.html', contexto)

def cosina(request):
    pedidos = Pedido.objects.all()
    contexto = {
        'pedidos':pedidos
    }
    return render(request, 'core/cosina.html', contexto)


@login_required
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
            messages.success(request, "Plato creado correctamente")
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
            messages.success(request, "Plato modificado correctamente")
            contexto['mensaje'] = "Modificado Correctamente"


    return render (request, 'core/form_mod_plato.html',contexto)

def form_del_plato(request,id):
    plato = Plato.objects.get(idPlato = id)

    plato.delete()
    messages.success(request, "Plato eliminado correctamente")

    return redirect (to="home")


    ###########################################


def reserva(request):
    reservas = Reservacion.objects.all()
    contexto = {
        'reservas':reservas
    }
    return render(request,'core/reserva.html', contexto)

def form_reserva(request):
    formulario = ReservacionForm()
    
    contexto = {
        'form':ReservacionForm()
    }
    if request.method == 'POST':
        formulario = ReservacionForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            messages.success(request, "Reserva creada correctamente")
            contexto['mensaje'] = "Guardado Correctamente"
    return render(request,'core/form_reserva.html', contexto)

def form_mod_reserva(request,id):
    reservacion = Reservacion.objects.get(idReservacion= id)

    contexto = {
        'form' : ReservacionForm(instance=reservacion)
    }

    if request.method == 'POST':
        formulario = ReservacionForm(data=request.POST,instance=reservacion)
        if formulario.is_valid:
            formulario.save()
            messages.success(request, "Reserva modificada correctamente")
            messages.success(request, "Reserva modificada correctamente")

            contexto['mensaje'] = "Modificado Correctamente"


    return render (request, 'core/form_mod_reserva.html',contexto)

def form_del_reserva(request,id):
    reserva = Reservacion.objects.get(idReservacion = id)

    reserva.delete()
    messages.success(request, "Reserva eliminada correctamente")

    return redirect (to="reserva")


##########################################

def bodega(request):
    bodegas = Bodega.objects.all()
    contexto = {
        'bodegas':bodegas
    }
    return render(request,'core/bodega.html', contexto)

def form_bodega(request):
    formulario = BodegaForm()
    
    contexto = {
        'form':BodegaForm()
    }
    if request.method == 'POST':
        formulario = BodegaForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            messages.success(request, "Producto creado correctamente")
            contexto['mensaje'] = "Guardado Correctamente"
    return render(request,'core/form_bodega.html', contexto)

def form_mod_bodega(request,id):
    bodega = Bodega.objects.get(idProducto= id)

    contexto = {
        'form' : BodegaForm(instance=bodega)
    }

    if request.method == 'POST':
        formulario = BodegaForm(data=request.POST,instance=bodega)
        if formulario.is_valid:
            formulario.save()
            messages.success(request, "Producto modificado correctamente")
            contexto['mensaje'] = "Modificado Correctamente"


    return render (request, 'core/form_mod_bodega.html',contexto)

def form_del_bodega(request,id):
    bodega = Bodega.objects.get(idProducto = id)

    bodega.delete()
    messages.success(request, "Producto eliminado correctamente")

    return redirect (to="bodega")


def form_pedido(request):
    formulario = PedidoForm()
    contexto = {
        'form':PedidoForm()
    }
    if request.method == 'POST':
        formulario = PedidoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            messages.success(request, "Pedido enviado")
            contexto['mensaje'] = "Guardado Correctamente"
    return render(request,'core/form_pedido.html', contexto)


def form_mod_pedido(request,id):
    pedido = Pedido.objects.get(idPedido = id)

    contexto = {
        'form' : CocinaForm(instance=pedido)
    }

    if request.method == 'POST':
        formulario = CocinaForm(data=request.POST,instance=pedido)
        if formulario.is_valid:
            formulario.save()
            messages.success(request, "Pedido modificado correctamente")
            contexto['mensaje'] = "Modificado Correctamente"


    return render (request, 'core/form_mod_pedido.html',contexto)


def form_del_pedido(request,id):
    pedido = Pedido.objects.get(idPedido = id)

    pedido.delete()
    messages.success(request, "Pedido eliminado correctamente")


    return redirect (to="cosina")

    ###########################3

def form_receta(request):
    formulario = RecetaForm()
    contexto = {
        'form':RecetaForm()
    }
    if request.method == 'POST':
        formulario = RecetaForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            messages.success(request, "Receta creada correctamente")
            messages.success(request, "receta enviado")
            contexto['mensaje'] = "Guardado Correctamente"
    return render(request,'core/form_receta.html', contexto)


def form_mod_receta(request,id):
    receta = Receta.objects.get(idReceta = id)

    contexto = {
        'form' : RecetaForm(instance=receta)
    }

    if request.method == 'POST':
        formulario = RecetaForm(data=request.POST,instance=receta)
        if formulario.is_valid:
            formulario.save()
            messages.success(request, "Receta modificada correctamente")

            contexto['mensaje'] = "Modificado Correctamente"


    return render (request, 'core/form_mod_receta.html',contexto)


def form_del_receta(request,id):
    receta = Receta.objects.get(idReceta = id)

    receta.delete()
    messages.success(request, "Receta eliminada correctamente")


    return redirect (to="receta")


