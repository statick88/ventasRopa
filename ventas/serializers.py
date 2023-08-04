from rest_framework import serializers
from .models import Cliente, Producto, Venta

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        # fields = ('id', 'nombre', 'apellido', 'email', 'telefono')
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class VentaSerializer(serializers.ModelSerializer):
    total = serializers.ReadOnlyField()

    class Meta:
        model = Venta
        fields = '__all__'
