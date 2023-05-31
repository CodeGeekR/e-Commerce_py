from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.models import User
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny

from .models import Producto, Categoria
from django.contrib.auth.models import Group, User

from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, UpdateAPIView, ListAPIView, \
    RetrieveUpdateDestroyAPIView, DestroyAPIView
from .serializers import ProductoSerializer, CategoriaSerializer


class UserListView(ListView):
    model = User  # Especifica el modelo a utilizar (User en este caso)
    template_name = 'user_list.html'  # Especifica el nombre de la plantilla para mostrar la lista de usuarios
    context_object_name = 'object_list'  # Especifica el nombre de la variable de contexto para la lista de usuarios
    paginate_by = 10  # Especifica el número de usuarios por página
    queryset = User.objects.all()  # Especifica la consulta para obtener la lista de usuarios
    ordering = ['username']  # Especifica el ordenamiento de la lista de usuarios


@permission_classes((AllowAny,))
class productoListApi(ListAPIView):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.filter(precio__lte=5000000, precio__gte=1000000)


@permission_classes((AllowAny,))
class categoriaListApi(ListAPIView):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all().order_by('nombreCategoria')
