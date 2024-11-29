from rest_framework import serializers

from .models import Productos

class ProductosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Productos
        fields = ['id', 'nombre', 'descripcion', 'precio_original', 'precio_descuento', 'stock', 'categoria', 'marca', 'nuevo', 'fecha_creacion']