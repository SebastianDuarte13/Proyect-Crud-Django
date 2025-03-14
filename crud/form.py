from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion',  ]
        # fields = '__all__' # Para seleccionar todos los campos