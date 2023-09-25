from django.db import models

class Usuario(models.Model):
    ESTADOS = (
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    )
    ROLES = (
        ('Mesero', 'Mesero'),
        ('Bartender', 'Bartender'),
        ('Administrador', 'Administrador'),
    )
    numero_identificacion = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    rol = models.CharField(max_length=20, choices=ROLES)
    telefono = models.CharField(max_length=15)
    estado = models.CharField(max_length=10, choices=ESTADOS, default='Activo')

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_inventario = models.IntegerField()

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    direccion = models.TextField()
    email = models.EmailField()
    telefono = models.CharField(max_length=15)

class Orden(models.Model):
    ESTADOS = (
        ('En preparación', 'En preparación'),
        ('Completada', 'Completada'),
        ('Cancelada', 'Cancelada'),
    )
    mesero = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='En preparación')
    total = models.DecimalField(max_digits=10, decimal_places=2)

class DetalleOrden(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

class Factura(models.Model):
    orden = models.OneToOneField(Orden, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

class Venta(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_vendida = models.IntegerField()

class Inventario(models.Model):
    producto = models.OneToOneField(Producto, on_delete=models.CASCADE)
    cantidad_actual = models.IntegerField()
    fecha_ultima_actualizacion = models.DateTimeField(auto_now=True)

class Compra(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

class DetalleCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)