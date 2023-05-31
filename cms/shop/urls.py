from django.urls import path
from shop.views import UserListView
from django.urls import re_path
from .views import productoListApi
from .views import categoriaListApi


urlpatterns = [
    path("listView/", UserListView.as_view(), name="listView"),
    path("", UserListView.as_view(), name="listView"),
]

app_name = 'shop'

urlpatterns = [
    re_path(r"^getproducts$", productoListApi.as_view(), name="getproducts"),
    re_path(r"^getcategories", categoriaListApi.as_view(), name="getcategories"),
]
