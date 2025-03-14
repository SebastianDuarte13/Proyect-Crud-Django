from django.db import models

# Create your models here.

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    descripcion = models.TextField(verbose_name="Descripción", blank=True, null=True)
    stock = models.IntegerField(default=0)  # Siempre inicia en 0
    estado = models.IntegerField(choices=[(1, "Activo"), (0, "Inactivo")], default=1)

    class Meta:
        db_table = "productos"  # Aquí defines el nombre correcto

    def __str__(self):
        superior = "Producto: " + self.nombre
        return superior


#  class Proveedor(models.Model):
#     id = models.AutoField(primary_key=True)
#     nombre = models.CharField(max_length=100, verbose_name="Nombre")
#     estado = models.IntegerField(
#         choices=[(1, "Activo"), (0, "Inactivo")], 
#         default=1  # Siempre inicia en 1 (activo)
#     )


# class Suministro(models.Model):
#     producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
#     proveedor = models.ForeignKey('Proveedor', on_delete=models.CASCADE)
#     cantidad = models.IntegerField()

#     def save(self, *args, **kwargs):
#         # Aumentar el stock del producto al agregar un suministro
#         self.producto.stock += self.cantidad
#         self.producto.save()
#         super().save(*args, **kwargs)