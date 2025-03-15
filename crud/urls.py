from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),

    # aquí se solo las rutas de los productos

    path('productos/', views.productos, name='productos'),
    path('productos/crear', views.crear, name='crear'),
    path('productos/editar', views.editar, name='editar'),
    path('productos/eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('productos/editar/<int:id>/', views.editar, name='editar'),

    # aquí se solo las rutas de los proveedores

    path('proveedores/', views.proveedores, name='proveedores'),
    path('proveedores/crear', views.crear_proveedor, name='crear_proveedor'),
    path('proveedores/editar', views.editar_proveedor, name='editar_proveedor'),
    path('proveedores/eliminar/<int:id>', views.eliminar_proveedor, name='eliminar_proveedor'),
    path('proveedores/editar/<int:id>/', views.editar_proveedor, name='editar_proveedor'),

    # aquí se solo las rutas de los suministros

    path('suministros/', views.suministros, name='suministros'),
    path('suministros/crear', views.crear_suministro, name='crear_suministro'),
    path('suministros/editar', views.editar_suministro, name='editar_suministro'),
    path('suministros/eliminar/<int:id>', views.eliminar_suministro, name='eliminar_suministro'),
    path('suministros/editar/<int:id>/', views.editar_suministro, name='editar_suministro'),


]