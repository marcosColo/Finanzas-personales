from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='inicio'),                       # Pagina principal
    path('formIngreso/', views.formIng, name='nuevo_Ing'),          # Form para registrar nuevo ingreso
    path('formRegIngreso/', views.formRegIng, name='formRegIng'),   # Form para registrar nuevo ingreso dentro del registro de ingresos
    path('nuevoRegIngreso/', views.nuevoRegIngreso),  
    path('nuevoIngreso/', views.nuevoIngreso),                      # Logica para nuevo ingreso
    path('formGasto/', views.formGas, name='nuevo_Gas'),            # Form para registrar nuevo gasto
    path('nuevoGasto/', views.nuevoGasto),                          # Logica para nuevo gasto
    path('eliminar/<id>', views.eliminarIng),                       # Logica para eliminar ingreso
    path('eliminargas/<id>', views.eliminarGas),                    # Logica para eliminar gasto
    path('registroIngreso', views.regIng, name='regIng'),           # Pagina con todos los ingresos
    path('registroGasto', views.regGas, name='regGas'),             # Pagina con todos los gastos
]