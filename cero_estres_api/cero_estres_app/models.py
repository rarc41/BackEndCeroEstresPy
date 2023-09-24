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
