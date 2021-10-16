from django.contrib import admin
from .models.user import User
from .models.producto import Producto

admin.site.register(User)
admin.site.register(Producto)

# Register your models here.
