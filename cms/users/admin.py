from django.contrib import admin
from .models import User, Pais, Departamentos, Ciudades, Domicilio, Categoria, SubCategoria, Producto, Descuento, DetalleDescuento, CuponDescuento, FormadePago, EstadodeCompra, OrdendeCompra

admin.site.register(Pais)
admin.site.register(Departamentos)
admin.site.register(Ciudades)
admin.site.register(Domicilio)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Descuento)
admin.site.register(DetalleDescuento)
admin.site.register(CuponDescuento)
admin.site.register(FormadePago)
admin.site.register(EstadodeCompra)
admin.site.register(OrdendeCompra)
admin.site.register(SubCategoria)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'last_name', 'email', 'telephone_number', 'id_status', 'date_created')
    list_filter = ('id_status',)
    search_fields = ('name', 'last_name', 'email')

    def formatted_date_created(self, obj):
        return obj.formatted_date_created()

    formatted_date_created.short_description = 'Date Created'
    formatted_date_created.admin_order_field = 'date_created'



