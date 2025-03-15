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


class Proveedor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    estado = models.IntegerField(
        choices=[(1, "Activo"), (0, "Inactivo")], 
        default=1  # Siempre inicia en 1 (activo)
    )

    class Meta:
        db_table = "proveedores" 

    def __str__(self):
        superior = "Proveedor: " + self.nombre
        return superior


class Suministro(models.Model):
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    proveedor = models.ForeignKey('Proveedor', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)  

    def save(self, *args, **kwargs):
        # Obtener el suministro previo si existe
        if self.pk:
            suministro_anterior = Suministro.objects.get(pk=self.pk)
            diferencia = self.cantidad - suministro_anterior.cantidad  # Ajustar diferencia en stock
            self.producto.stock += diferencia
        else:
            # Si es un nuevo suministro, simplemente sumarlo
            self.producto.stock += self.cantidad

        self.producto.save()  # Guardar cambios en el producto
        super().save(*args, **kwargs)

    class Meta:
        db_table = "suministros"

   