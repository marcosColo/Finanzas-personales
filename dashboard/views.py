from django.shortcuts import render, redirect
from .models import ingresos, gastos, balance

# Create your views here.

# VIEWS
# VIEWS
# VIEWS
# VIEWS

# View de la pagina principal del dashboard
# =====================================================
def dashboard(request):
    dataIng = ingresos.objects.all()
    dataGas = gastos.objects.all()
    balact = ingresos.objects.values_list('monto', flat=True)
    balpas = gastos.objects.values_list('monto', flat=True)
    
    balAct = 0
    balPas = 0

    for i in balact:
        balAct = balAct + i

    for i in balpas:
        balPas = balPas + i

    balanceFinal = (balAct - balPas)

    contexto = {
        'a':dataIng,
        'b':dataGas,
        'c':balanceFinal,
    }

    return render(request, 'dashboard.html', {'contexto':contexto})

# =====================================================

# FORMULARIOS
# =====================================================
# Para registar nuevo ingreso
def formIng(request):
    return render (request, 'formIng.html')

# Para registrar nuevo gasto
def formGas(request):
    return render (request, 'formGas.html')

# =====================================================

# Views de los registros completos de ingresos y gastos
# =====================================================
# Ingresos
def regIng(request):
    dataIng = ingresos.objects.all()
    balact = ingresos.objects.values_list('monto', flat=True)
    
    balAct = 0

    for i in balact:
        balAct = balAct + i

    contexto = {
        'a':dataIng,
        'b':balAct
    }

    return render(request, 'regIng.html', {'contexto':contexto})

# Para registar nuevo ingreso dentro del registro de ingresos
def formRegIng(request):
    return render (request, 'formRegIng.html')

# Gastos
def regGas(request):
    dataGas = gastos.objects.all()
    balpas = gastos.objects.values_list('monto', flat=True)
    
    balPas = 0

    for i in balpas:
        balPas = balPas + i

    contexto = {
        'b':dataGas,

    }

    return render(request, 'regGas.html', {'contexto':contexto})

# Boton de eliminar dentro del registro de ingresos
def elimiRegIng(request, id):
    registro = ingresos.objects.get(id=id)
    registro.delete()

    return redirect('regIng.html')

# Boton de eliminar dentro del registro de gastos
def elimiRegGas(request, id):
    registro = gastos.objects.get(id=id)
    registro.delete()

    return redirect('/')
# =====================================================
# =====================================================

#   LOGICA
#   LOGICA
#   LOGICA
#   LOGICA
# =====================================================
# Para eliminar un ingreso ya creado (la cruz que esta en cada card)
def eliminarIng(request, id):
    registro = ingresos.objects.get(id=id)
    registro.delete()

    return redirect('/')

# Para eliminar un gasto ya creado
def eliminarGas(request, id):
    registro = gastos.objects.get(id=id)
    registro.delete()

    return redirect('/')

# Logica para crear un nuevo registro (objeto) de ingreso (instancia la clase (modelo) ingresos)
def nuevoIngreso(request):
    detalle = request.POST.get('ingreso-Detalle', False)
    monto = request.POST.get('ingMonto', False)

    nuevo_ingreso = ingresos.objects.create(detalle=detalle, monto=monto)
    return redirect('/')

# Logica para crear un nuevo ingreso DENTRO de la pagina donde estan todos los registros de ingreso
def nuevoRegIngreso(request):
    detalle = request.POST.get('ingreso-Detalle', False)
    monto = request.POST.get('ingMonto', False)

    nuevo_ingreso = ingresos.objects.create(detalle=detalle, monto=monto)
    return redirect('registroIngreso/')

# Logica para crear un nuevo registro de gasto (instancia a gastos)
def nuevoGasto(request):
    detalle = request.POST.get('gasto-Detalle', False)
    monto = request.POST.get('gasMonto', False)

    nuevo_ingreso = gastos.objects.create(detalle=detalle, monto=monto)
    return redirect('/')
# =====================================================

