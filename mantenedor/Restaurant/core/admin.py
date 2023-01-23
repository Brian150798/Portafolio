from django.contrib import admin
from .models import Categoria, Plato, Reservacion, Hora, Fecha, Bodega, Estado, Pedido, Receta,Usuario, Disponible, Mesa, ProTipo, Proveedor, Producto
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Plato)
admin.site.register(Reservacion)
admin.site.register(Hora)
admin.site.register(Fecha)
admin.site.register(Bodega)
admin.site.register(Estado)
admin.site.register(Pedido)
admin.site.register(Receta)
admin.site.register(Usuario)
admin.site.register(Disponible)
admin.site.register(Mesa)
admin.site.register(ProTipo)
admin.site.register(Proveedor)
admin.site.register(Producto)

