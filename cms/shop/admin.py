from django.contrib import admin

from .models import Profile, Pais, Departamentos, Ciudades, Categoria, SubCategoria, Producto, Descuento, \
    DetalleDescuento, FormadePago, EstadodeCompra, OrdendeCompra, CuponDescuento

admin.site.register(Pais)
admin.site.register(Departamentos)
admin.site.register(Ciudades)
admin.site.register(Categoria)
# admin.site.register(Producto)
# admin.site.register(Descuento)
# admin.site.register(DetalleDescuento)
# admin.site.register(CuponDescuento)
admin.site.register(FormadePago)
admin.site.register(EstadodeCompra)
# admin.site.register(OrdendeCompra)
admin.site.register(SubCategoria)


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'address', 'city', 'telephone_number', 'id_status', 'user_group')
    search_fields = ('city', 'user__username', 'user__groups__name')
    list_filter = ('city', 'user__groups',)

    def user_group(self, obj):
        return " - ".join([t.name for t in obj.user.groups.all().order_by("name")])

    user_group.short_description = 'Groups'


admin.site.register(Profile, ProfileAdmin)


@admin.register(CuponDescuento)
class CuponDescuentoAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'code_cupon', 'description', 'id_status', 'date_end')
    list_filter = ('id_status',)
    search_fields = ('code_cupon',)

    def formatted_date_created(self, obj):
        return obj.formatted_date_created()

    formatted_date_created.short_description = 'Date Created'
    formatted_date_created.admin_order_field = 'date_created'


@admin.register(Descuento)
class DescuentoAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'nombreProducto', 'precio', 'porcentaje', 'id_status', 'date_end')
    list_filter = ('id_status',)
    search_fields = ('id_producto',)

    def formatted_date_created(self, obj):
        return obj.formatted_date_created()

    formatted_date_created.short_description = 'Date Created'
    formatted_date_created.admin_order_field = 'date_created'

    def nombreProducto(self, obj):
        return "{}".format(obj.id_producto.nombreProducto)

    nombreProducto.short_description = 'Producto'

    def precio(self, obj):
        return "${}".format(obj.id_producto.precio)

    precio.short_description = 'Precio'


@admin.register(DetalleDescuento)
class DetalleDescuentoAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'producto', 'precio', 'porcentaje', 'id_status')
    list_filter = ('id_status',)
    search_fields = ('id_descuento', 'id_producto')

    def formatted_date_created(self, obj):
        return obj.formatted_date_created()

    formatted_date_created.short_description = 'Date Created'
    formatted_date_created.admin_order_field = 'date_created'

    def producto(self, obj):
        return "{}".format(obj.id_producto.nombreProducto)

    producto.short_description = 'Producto'

    def precio(self, obj):
        return "${}".format(obj.id_producto.precio)

    precio.short_description = 'Precio'

    def porcentaje(self, obj):
        return "{}%".format(obj.id_descuento.porcentaje)

    porcentaje.short_description = 'Porcentaje'


@admin.register(OrdendeCompra)
class OrdendeCompraAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'id_user', 'nombre_producto', 'precio_producto', 'forma_pago', 'estado_compra', 'date_created',)
    list_filter = ('id_status',)
    search_fields = ('id_user', 'id_status')

    def formatted_date_created(self, obj):
        return obj.formatted_date_created()

    formatted_date_created.short_description = 'Date Created'
    formatted_date_created.admin_order_field = 'date_created'

    def nombre_producto(self, obj):
        return "{}".format(obj.id_producto.nombreProducto)

    nombre_producto.short_description = 'Producto'

    def precio_producto(self, obj):
        return "${}".format(obj.id_producto.precio)

    precio_producto.short_description = 'Precio'

    def forma_pago(self, obj):
        return "{}".format(obj.id_forma_pago.formas_pago)

    forma_pago.short_description = 'Forma de Pago'

    def estado_compra(self, obj):
        return "{}".format(obj.id_estado_compra.estado_compra)

    estado_compra.short_description = 'Estado de Compra'


def categoria(obj):
    return "{}".format(obj.id_categoria.nombreCategoria)


def categoria(obj):
    return "{}".format(obj.id_subcategoria.id_categoria.nombreCategoria)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'nombreProducto', 'precio', 'cantidad', 'id_status', 'date_created')
    list_filter = ('id_status',)
    search_fields = ('nombreProducto', 'id_subcategoria')

    def formatted_date_created(self, obj):
        return obj.formatted_date_created()

    formatted_date_created.short_description = 'Date Created'
    formatted_date_created.admin_order_field = 'date_created'

# @admin.register(Domicilio)
# class DomicilioAdmin(admin.ModelAdmin):
#    list_display = (
#        'id', 'id_user', 'ciudad', 'direccion', 'id_status', 'date_created')
#    list_filter = ('id_status',)
#    search_fields = ('id_user', 'id_ciudad', 'direccion')
#
#    def formatted_date_created(self, obj):
#        return obj.formatted_date_created()
#
#    formatted_date_created.short_description = 'Date Created'
#    formatted_date_created.admin_order_field = 'date_created'
#
#    def ciudad(self, obj):
#        return "{}".format(obj.id_ciudad.nombreCiudad)
#
#    ciudad.short_description = 'ciudad'
