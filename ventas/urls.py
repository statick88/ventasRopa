from django.urls import path
from .views import listar_clientes, listar_productos, listar_ventas
# from . import views

urlpatterns = [
    # path('clientes/', views.listar_clientes, name='clientes'),
    path('clientes/', listar_clientes, name='clientes'),
    # path('productos/', views.listar_productos, name='productos'),
    path('productos/', listar_productos, name='productos'),
    # path('ventas/', views.listar_ventas, name='ventas'),
    path('ventas/', listar_ventas, name='ventas'),
]