from django.urls import path
from shop.views import UserListView

urlpatterns = [
    path("listView/", UserListView.as_view(), name="listView"),
]
