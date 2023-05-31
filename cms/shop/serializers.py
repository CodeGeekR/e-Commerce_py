from .models import Profile, Domicilio, Categoria, SubCategoria, Producto, Descuento, OrdendeCompra
from django.contrib.auth.models import Group, User

from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.serializers import (
    SerializerMethodField
)


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class ProductoSerializer(ModelSerializer):
    id_categoria = CategoriaSerializer(many=False)
    class Meta:
        model = Producto
        fields = '__all__'