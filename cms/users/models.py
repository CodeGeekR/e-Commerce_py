from django.db import models
from django.utils import timezone


# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    telephone_number = models.CharField(max_length=50, default='')
    id_status = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'User ({self.id}): {self.name} {self.last_name}'

    def formatted_date_created(self):
        return self.date_created.strftime('%Y-%B-%d %H:%M:%S')


class Pais(models.Model):
    id = models.AutoField(primary_key=True)
    nombrePais = models.CharField(max_length=50)
    id_status = models.BooleanField(default=True)

    def __str__(self):
        return f'Pais ({self.id}): {self.nombrePais}'


class Departamentos(models.Model):
    id = models.AutoField(primary_key=True)
    id_pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    nombreDepartamento = models.CharField(max_length=50)
    indicativo = models.IntegerField(default=0)
    id_status = models.BooleanField(default=True)

    def __str__(self):
        return f'Departamentos ({self.id_pais}): {self.nombreDepartamento} {self.indicativo} {self.id_status}'


class Ciudades(models.Model):
    id = models.AutoField(primary_key=True)
    id_departamento = models.ForeignKey(Departamentos, on_delete=models.CASCADE)
    nombreCiudad = models.CharField(max_length=50)
    id_status = models.BooleanField(default=True)

    def __str__(self):
        return f'Ciudades ({self.id_departamento}): {self.nombreCiudad} {self.id_status}'


class Domicilio(models.Model):
    id = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_ciudad = models.ForeignKey(Ciudades, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=100)
    barrio = models.CharField(max_length=50)
    id_status = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Domicilio ({self.id_user}): {self.direccion} {self.barrio} {self.id_status}'

    def formatted_date_created(self):
        return self.date_created.strftime('%Y-%B-%d %H:%M:%S')


class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombreCategoria = models.CharField(max_length=50)
    id_status = models.BooleanField(default=True)

    def __str__(self):
        return f'Categoria ({self.id}): {self.nombreCategoria} {self.id_status}'


class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombreProducto = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    precio = models.IntegerField(default=0)
    cantidad = models.IntegerField(default=0)
    id_status = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Producto ({self.id_categoria}): {self.nombreProducto} {self.precio} {self.cantidad} {self.id_status}'

    def formatted_date_created(self):
        return self.date_created.strftime('%Y-%B-%d %H:%M:%S')


class Descuento(models.Model):
    id = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    porcentaje = models.IntegerField(default=0)
    id_status = models.BooleanField(default=True)
    date_start = models.DateTimeField(default=timezone.now)
    date_end = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Descuento ({self.id_producto}): {self.porcentaje} % {self.date_start} - {self.date_end}'


class DetalleDescuento(models.Model):
    id = models.AutoField(primary_key=True)
    id_descuento = models.ForeignKey(Descuento, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    id_status = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'DetalleDescuento ({self.id}): {self.id_descuento} {self.id_producto} {self.id_status}'

    def formatted_date_created(self):
        return self.date_created.strftime('%Y-%B-%d %H:%M:%S')


class CuponDescuento(models.Model):
    id = models.AutoField(primary_key=True)
    name_cupon = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    id_status = models.BooleanField(default=True)
    date_start = models.DateTimeField(default=timezone.now)
    date_end = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'CuponDescuento ({self.id}): {self.name_cupon} {self.description} {self.date_start} - {self.date_end}'


class FormadePago(models.Model):
    id = models.AutoField(primary_key=True)
    formas_pago = models.CharField(max_length=50)
    id_status = models.BooleanField(default=True)

    def __str__(self):
        return f'FormadePago ({self.id}): {self.formas_pago} {self.id_status}'


class EstadodeCompra(models.Model):
    id = models.AutoField(primary_key=True)
    estado_compra = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    id_status = models.BooleanField(default=True)

    def __str__(self):
        return f'EstadodeCompra ({self.id}): {self.estado_compra} {self.descripcion} {self.id_status}'


class OrdendeCompra(models.Model):
    id = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_domicilio = models.ForeignKey(Domicilio, on_delete=models.CASCADE)
    id_forma_pago = models.ForeignKey(FormadePago, on_delete=models.CASCADE)
    id_estado_compra = models.ForeignKey(EstadodeCompra, on_delete=models.CASCADE)
    id_status = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'OrdendeCompra ({self.id_user}): {self.id_forma_pago} {self.id_estado_compra} {self.id_status}'

    def formatted_date_created(self):
        return self.date_created.strftime('%Y-%B-%d %H:%M:%S')
