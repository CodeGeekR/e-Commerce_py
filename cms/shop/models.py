from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.db.models.signals import post_save


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
        return f'Departamentos ({self.id}): {self.nombreDepartamento} {self.indicativo} {self.id_status}'


class Ciudades(models.Model):
    id = models.AutoField(primary_key=True)
    id_departamento = models.ForeignKey(Departamentos, on_delete=models.CASCADE)
    nombreCiudad = models.CharField(max_length=50)
    id_status = models.BooleanField(default=True)

    def __str__(self):
        return f'Ciudades ({self.id}): {self.nombreCiudad} {self.id_status}'


def validate_imagenProfile_resolution(image_profile):
    width, height = image_profile.width, image_profile.height
    if width > 600 or height > 600:
        raise ValidationError("La imagen debe tener una resolución máxima de 600x600 píxeles.")


class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    imagenProfile = models.ImageField(upload_to='profile/', null=True, blank=True, validators=[validate_imagenProfile_resolution])
    telephone_number = models.CharField(max_length=50, default='')
    address = models.CharField(max_length=100, default='')
    department = models.ForeignKey(Departamentos, on_delete=models.SET_NULL, blank=True, null=True)
    city = models.ForeignKey(Ciudades, on_delete=models.SET_NULL, blank=True, null=True)
    id_status = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        ordering = ['-date_created']

    #
    def __str__(self):
        return f'User ({self.user}):  {self.telephone_number}'

    def get_available_cities(self):
        if self.department:
            return Ciudades.objects.filter(id_departamento=self.department)
        else:
            return Ciudades.objects.none()

# ESTE CODIGO ES PARA CREAR UN PERFIL DE USUARIO AUTOMATICAMENTE AL CREAR UN USUARIO USANDO SIGNALS.PY
# def create_profile(sender, instance, created,  **kwargs):
#    if created:
#        Profile.objects.get_or_create(user=instance)
#
#
# def save_profile(sender, instance, **kwargs):
#    instance.profile.save()
#
#
# post_save.connect(create_profile, sender=User)
# post_save.connect(save_profile, sender=User)


class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombreCategoria = models.CharField(max_length=50)
    id_status = models.BooleanField(default=True)

    def __str__(self):
        return f'Categoria ({self.id}): {self.nombreCategoria} {self.id_status}'


class SubCategoria(models.Model):
    id = models.AutoField(primary_key=True)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombreSubCategoria = models.CharField(max_length=50)
    id_status = models.BooleanField(default=True)

    def __str__(self):
        return f'SubCategoria ({self.id}): {self.nombreSubCategoria} {self.id_status}'


def validate_image_resolution(image):
    width, height = image.width, image.height
    if width > 1081 or height > 1081:
        raise ValidationError("La imagen debe tener una resolución máxima de 1080x1080 píxeles.")


# (Categoria, on_delete=models.CASCADE)
class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    id_categoria = models.ManyToManyField(Categoria)  # related_name='categoria', blank=True, null=True
    id_subcategoria = models.ForeignKey(SubCategoria, on_delete=models.SET_NULL, blank=True, null=True)
    nombreProducto = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='images/', null=True, blank=True, validators=[validate_image_resolution])
    precio = models.IntegerField(default=0)
    cantidad = models.IntegerField(default=0)
    id_status = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Producto ({self.id}): {self.nombreProducto} {self.precio} {self.cantidad} {self.id_status}'

    def formatted_date_created(self):
        return self.date_created.strftime('%Y-%B-%d %H:%M:%S')

    def formatted_price(self):
        return f'$ {self.precio} COP'


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


class CuponDescuento(models.Model):
    id = models.AutoField(primary_key=True)
    code_cupon = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    id_status = models.BooleanField(default=True)
    date_start = models.DateTimeField(default=timezone.now)
    date_end = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'CuponDescuento ({self.id}): {self.code_cupon} {self.description} {self.date_start} - {self.date_end} {self.id_status}'

    def formatted_date_start(self):
        return self.date_start.strftime('%Y-%B-%d')

    def formatted_date_end(self):
        return self.date_end.strftime('%Y-%B-%d')


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
        return f'EstadodeCompra ({self.id}): {self.estado_compra}'


class OrdendeCompra(models.Model):
    id = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE, default=1)
    cantidad = models.IntegerField(default=0)
    id_forma_pago = models.ForeignKey(FormadePago, on_delete=models.CASCADE)
    id_cupon_descuento = models.ForeignKey(CuponDescuento, on_delete=models.SET_NULL, null=True, blank=True)
    id_descuento = models.ForeignKey(Descuento, on_delete=models.SET_NULL, null=True, blank=True)
    id_estado_compra = models.ForeignKey(EstadodeCompra, on_delete=models.CASCADE)
    id_status = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'OrdendeCompra ({self.id}): {self.id_user} {self.id_producto} {self.cantidad}'

    def formatted_date_created(self):
        return self.date_created.strftime('%Y-%B-%d %H:%M:%S')

    def descuento_porcentaje(self):
        if self.id_descuento:
            return "{}%".format(self.id_descuento.porcentaje)
        else:
            return "0%"
