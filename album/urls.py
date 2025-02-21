from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('add', views.add_album, name="add_album"),
    path('edit/<int:id>', views.edit_album, name="edit_album"),
    path('del/<int:id>', views.del_album, name="del_album"),
]
