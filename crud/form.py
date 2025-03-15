from django import forms
from .models import Producto, Proveedor, Suministro


# Formulario para crear un producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion',  ]
        # fields = '__all__' # Para seleccionar todos los campos

# Formulario para editar un producto

class ProductoFormeditar(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'estado' ]
        # fields = '__all__' 

#formulario para crear un proveedor

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre',  ]
       

# Formulario para editar un producto

class ProveedorFormeditar(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'estado' ]

# Formulario para crear suministro

class SuministroForm(forms.ModelForm):
    class Meta:
        model = Suministro
        fields = '__all__'
        

class SuministroFormeditar(forms.ModelForm):
    class Meta:
        model = Suministro
        fields = '__all__'
