from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='inicio'),                
    path('formIngreso/', views.formIng, name='nuevo_Ing'),        
    path('nuevoRegIngreso/', views.nuevoRegIngreso), 
    path('nuevoRegGasto/', views.nuevoRegGasto),
    path('nuevoIngreso/', views.nuevoIngreso),                    
    path('formGasto/', views.formGas, name='nuevo_Gas'),         
    path('nuevoGasto/', views.nuevoGasto),                          
    path('eliminar/<id>', views.eliminarIng),                 
    path('eliminargas/<id>', views.eliminarGas),              
    path('eliminarRegIng/<id>', views.eliminarRegIng),
    path('eliminarRegGas/<id>', views.eliminarRegGas),
    path('registroIngreso', views.regIng, name='regIng'),         
    path('registroGasto', views.regGas, name='regGas'),            
]