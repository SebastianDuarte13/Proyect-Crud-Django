from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Producto, Proveedor, Suministro
from .form import ProductoForm, ProductoFormeditar, ProveedorForm, ProveedorFormeditar, SuministroForm, SuministroFormeditar

# Create your views here.

def inicio(request):
    # Renderiza la página de inicio
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    # Renderiza la página de información sobre la empresa
    return render(request, 'paginas/nosotros.html')

# Aquí se crean las funciones para manejar los productos

def productos(request):
    # Obtiene todos los productos de la base de datos
    productos = Producto.objects.all()
    return render(request, 'productos/indexp.html', {'productos': productos})

def crear(request):
    # Procesa el formulario para crear un nuevo producto
    formulario = ProductoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():  # Si el formulario es válido, guarda el producto
        formulario.save()
        return redirect('productos')  # Redirige a la lista de productos
    return render(request, 'productos/crear.html', {'formulario': formulario})

def editar(request, id):
    # Obtiene el producto a editar por su ID
    producto = Producto.objects.get(id=id)
    formulario = ProductoFormeditar(request.POST or None, request.FILES or None, instance=producto)
    if formulario.is_valid() and request.POST:  # Si el formulario es válido, guarda los cambios
        formulario.save()
        return redirect('productos')  # Redirige a la lista de productos
    return render(request, 'productos/editar.html', {'formulario': formulario})

def eliminar(request, id):
    # Obtiene el producto por su ID y lo elimina
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('productos')  # Redirige a la lista de productos


# aqui se crean las funciones para los proveedores

def proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedores/indexpr.html', {'proveedores': proveedores})

def crear_proveedor(request):
    formulario = ProveedorForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('proveedores')
    return render(request, 'proveedores/crear.html', {'formulario': formulario})

def editar_proveedor(request, id):
    proveedor = Proveedor.objects.get(id=id)
    formulario = ProveedorFormeditar(request.POST or None, request.FILES or None, instance=proveedor)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('proveedores')
    return render(request, 'proveedores/editar.html', {'formulario': formulario})

def eliminar_proveedor(request, id):
    proveedor = Proveedor.objects.get(id=id)
    proveedor.delete()
    return redirect('proveedores')

# aqui se crean las funciones de suministros

def suministros(request):
    suministros = Suministro.objects.all()
    return render(request, 'suministros/indexs.html', {'suministros': suministros})

def crear_suministro(request):
    formulario = SuministroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('proveedores')
    return render(request, 'proveedores/crear.html', {'formulario': formulario})

def editar_suministro(request, id):
    suministro = Suministro.objects.get(id=id)
    formulario = SuministroFormeditar(request.POST or None, request.FILES or None, instance=suministro)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('suministros')
    return render(request, 'suministros/editar.html', {'formulario': formulario})

def eliminar_suministro(request, id):
    suministro = Suministro.objects.get(id=id)
    suministro.delete()
    return redirect('suministros')

