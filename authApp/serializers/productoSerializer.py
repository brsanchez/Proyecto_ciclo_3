from authApp.models.producto import Producto
from rest_framework import serializers
from authApp.models.user import User
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio']

    def to_representation(self, obj):
        producto = Producto.objects.get(id=obj.id) #mirar más tarde
        #user = User.objects.get(id=obj.user_id)
        return{
            'id' : producto.id,
            'nombre' : producto.nombre,
            'precio' : producto.precio
            #'user'   : producto.user
        }