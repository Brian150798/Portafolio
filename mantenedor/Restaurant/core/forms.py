from django import forms
from django.forms import ModelForm
from .models import Plato

class PlatoForm(ModelForm):
    class Meta:
        model = Plato
        fields = ['idPlato','nombrePlato','valorPlato','categoria']