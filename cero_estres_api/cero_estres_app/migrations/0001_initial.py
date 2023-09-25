# Generated by Django 4.2.5 on 2023-09-24 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_hora', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_hora', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cantidad_inventario', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('contacto', models.CharField(max_length=100)),
                ('direccion', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_identificacion', models.CharField(max_length=20, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('rol', models.CharField(choices=[('Mesero', 'Mesero'), ('Bartender', 'Bartender'), ('Administrador', 'Administrador')], max_length=20)),
                ('telefono', models.CharField(max_length=15)),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_vendida', models.IntegerField()),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cero_estres_app.factura')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cero_estres_app.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_hora', models.DateTimeField(auto_now_add=True)),
                ('estado', models.CharField(choices=[('En preparación', 'En preparación'), ('Completada', 'Completada'), ('Cancelada', 'Cancelada')], default='En preparación', max_length=20)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mesero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cero_estres_app.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_actual', models.IntegerField()),
                ('fecha_ultima_actualizacion', models.DateTimeField(auto_now=True)),
                ('producto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cero_estres_app.producto')),
            ],
        ),
        migrations.AddField(
            model_name='factura',
            name='orden',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cero_estres_app.orden'),
        ),
        migrations.CreateModel(
            name='DetalleOrden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('orden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cero_estres_app.orden')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cero_estres_app.producto')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('precio_compra', models.DecimalField(decimal_places=2, max_digits=10)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cero_estres_app.compra')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cero_estres_app.producto')),
            ],
        ),
        migrations.AddField(
            model_name='compra',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cero_estres_app.proveedor'),
        ),
    ]