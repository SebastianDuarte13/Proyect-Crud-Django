from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('productos/', views.productos, name='productos'),
    path('productos/crear', views.crear, name='crear'),
    path('productos/editar', views.editar, name='editar'),
    path('productos/eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('productos/editar/<int:id>/', views.editar, name='editar'),

]