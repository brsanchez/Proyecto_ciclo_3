from rest_framework import serializers
from authApp.models import producto
from authApp.models.producto import Producto
from authApp.models.user import User
from authApp.models.account import Account
from authApp.serializers.accountSerializer import AccountSerializer

class UserSerializer(serializers.ModelSerializer):
    account = AccountSerializer()
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'name', 'email', 'producto']
 
    def create(self, validated_data):
        productoData = validated_data.pop('producto')
        userInstance = User.objects.create(**validated_data)
        Producto.objects.create(user=userInstance, **productoData)
        return userInstance
    
    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        producto = Producto.objects.get(user=obj.id)
        return {
                    'id': user.id,
                    'username': user.username,
                    'name': user.name,
                    'email': user.email,
                    'producto': {
                        'nombre': producto.nombre,
                        'precio': producto.precio,
                    }
                }

    