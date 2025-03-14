from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Producto
from .form import ProductoForm

# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')
def productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/indexp.html', {'productos': productos})
def crear(request):
    formulario = ProductoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('productos')
    return render(request, 'productos/crear.html', {'formulario': formulario})
def editar(request):
    return render(request, 'productos/editar.html')