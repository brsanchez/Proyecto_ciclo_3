from django.db import models
from .user import User

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='producto_user', on_delete=models.CASCADE)
    nombre = models.CharField(max_length = 15)
    precio = models.IntegerField()