from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('formIngreso/', views.formIng, name='nuevo_Ing'),
    path('nuevoIngreso/', views.nuevoIngreso),
    path('formGasto/', views.formGas, name='nuevo_Gas'),
    path('nuevoGasto/', views.nuevoGasto),
    path('eliminar/<id>', views.eliminarIng),
    path('eliminargas/<id>', views.eliminarGas),
]