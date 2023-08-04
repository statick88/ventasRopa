from django.urls import path
from .views import listar_clientes, listar_productos, listar_ventas
from .views import ClienteListCreateView, ClienteRetrieveUpdateDestroyView, ProductoListCreateView, ProductoRetrieveUpdateDestroyView, VentaListCreateView, VentaRetrieveUpdateDestroyView
# from . import views

urlpatterns = [
    path('clientes/', listar_clientes, name='clientes'),
    path('productos/', listar_productos, name='productos'),
    path('ventas/', listar_ventas, name='ventas'),

    path('', ClienteListCreateView.as_view(), name='cliente-list-create'),
    path('api/clientes/', ClienteListCreateView.as_view(), name='cliente-list-create'),
    path('api/clientes/<int:pk>/', ClienteRetrieveUpdateDestroyView.as_view(), name='cliente-retrieve-update-destroy'),
    path('api/productos/', ProductoListCreateView.as_view(), name='producto-list-create'),
    path('api/productos/<int:pk>/', ProductoRetrieveUpdateDestroyView.as_view(), name='producto-retrieve-update-destroy'),
    path('api/ventas/', VentaListCreateView.as_view(), name='venta-list-create'),
    path('api/ventas/<int:pk>/', VentaRetrieveUpdateDestroyView.as_view(), name='venta-retrieve-update-destroy'),

]