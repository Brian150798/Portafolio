from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True,verbose_name="id de Categoria")
    nombreCategoria = models.CharField(max_length=70,verbose_name="Nombre de la Categoria")
    def __str__(self):
        return self.nombreCategoria


class Plato(models.Model):
    idPlato = models.IntegerField(primary_key=True,verbose_name="id de Plato")
    nombrePlato = models.CharField(max_length=70,verbose_name="Nombre del Plato")
    valorPlato = models.IntegerField(verbose_name="Valor del Plato")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombrePlato