from django.contrib import admin
from .models import Producto
# from .models import Suministro
from .models import Proveedor

# Register your models here.

admin.site.register(Producto)
# admin.site.register(Suministro)
admin.site.register(Proveedor)