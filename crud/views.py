from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Producto, Proveedor
from .form import ProductoForm, ProductoFormeditar, ProveedorForm, ProveedorFormeditar

# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

# aqui se crean las funciones para los productos

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/indexp.html', {'productos': productos})

def crear(request):
    formulario = ProductoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('productos')
    return render(request, 'productos/crear.html', {'formulario': formulario})

def editar(request, id):
    producto = Producto.objects.get(id=id)
    formulario = ProductoFormeditar(request.POST or None, request.FILES or None, instance=producto)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('productos')
    return render(request, 'productos/editar.html', {'formulario': formulario})

def eliminar(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('productos')

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
