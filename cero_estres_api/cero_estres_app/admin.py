# cero_estres_app/admin.py

from django.contrib import admin
from .models import Usuario, Producto, Proveedor, Orden, DetalleOrden, Factura, Venta, Inventario, Compra, DetalleCompra

admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(Orden)
admin.site.register(DetalleOrden)
admin.site.register(Factura)
admin.site.register(Venta)
admin.site.register(Inventario)
admin.site.register(Compra)
admin.site.register(DetalleCompra)
