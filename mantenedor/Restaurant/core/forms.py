from django import forms
from django.forms import ModelForm,widgets
from .models import Plato, Reservacion, Hora, Fecha, Bodega, Estado, Pedido, Receta, Mesa
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PlatoForm(ModelForm):
    class Meta:
        model = Plato
        fields = ['idPlato','nombrePlato','valorPlato','categoria']
        widgets={
            'idPlato' : forms.NumberInput(attrs={'class':'form-control'}),
            'nombrePlato' : forms.TextInput(attrs={'class':'form-control'}),
            'valorPlato' : forms.NumberInput(attrs={'class':'form-control'}),
            'categoria' : forms.Select(attrs={'class':'form-control'})
        }

class ReservacionForm(ModelForm):
    class Meta:
        model = Reservacion
        fields = ['idReservacion','nombreReservacion','fecha','hora',]
        widgets={
            'idReservacion' : forms.NumberInput(attrs={'class':'form-control'}),
            'nombreReservacion' : forms.TextInput(attrs={'class':'form-control'}),
            'fecha' : forms.Select(attrs={'class':'form-control'}),
            'hora' : forms.Select(attrs={'class':'form-control'}),
            
            
        }

class BodegaForm(ModelForm):
    class Meta:
        model = Bodega
        fields = ['idProducto','nombreProducto','cantidadProducto']
        widgets={
            'idProducto' : forms.NumberInput(attrs={'class':'form-control'}),
            'nombreProducto' : forms.TextInput(attrs={'class':'form-control'}),
            'cantidadProducto' : forms.NumberInput(attrs={'class':'form-control'})
        }

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','email','password1','password2']
        widgets={
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'first_name' : forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'password1' : forms.PasswordInput(attrs={'class':'form-control'}),
            'password2' : forms.PasswordInput(attrs={'class':'form-control'})
        
        }

class PedidoForm(ModelForm):
    class Meta:
        model = Pedido
        fields = ['idPedido','numeroMesa','nplato',]
        widgets={
            'idPedido' : forms.NumberInput(attrs={'class':'form-control'}),
            'numeroMesa' : forms.NumberInput(attrs={'class':'form-control'}),
            'nplato' : forms.Select(attrs={'class':'form-control'})
        }

class CocinaForm(ModelForm):
    class Meta:
        model = Pedido
        fields = ['idPedido','numeroMesa','nplato','estado']
        widgets={
            'idPedido' : forms.NumberInput(attrs={'class':'form-control'}),
            'numeroMesa' : forms.NumberInput(attrs={'class':'form-control'}),
            'nplato' : forms.Select(attrs={'class':'form-control'}),
            'estado' : forms.Select(attrs={'class':'form-control'})
        }

class RecetaForm(ModelForm):
    class Meta:
        model = Receta
        fields = ['idReceta','nombreReceta','descripcion']
        widgets={
            'idReceta' : forms.NumberInput(attrs={'class':'form-control'}),
            'nombreReceta' : forms.TextInput(attrs={'class':'form-control'}),
            'descripcion' : forms.Textarea(attrs={'class':'form-control'}),

        }
        
class MesaForm(ModelForm):
    class Meta:
        model = Mesa
        fields = ['idMesa','numeroMesa','ubicacion','descripcion','disponible']
    
        




