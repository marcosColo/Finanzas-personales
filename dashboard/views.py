from django.shortcuts import render, redirect
from .models import ingresos, gastos, balance

# Create your views here.
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

def formIng(request):
    return render (request, 'formIng.html')

def eliminarIng(request, id):
    registro = ingresos.objects.get(id=id)
    registro.delete()

    return redirect('/')

def eliminarGas(request, id):
    registro = gastos.objects.get(id=id)
    registro.delete()

    return redirect('/')

def nuevoIngreso(request):
    detalle = request.POST.get('ingreso-Detalle', False)
    monto = request.POST.get('ingMonto', False)

    nuevo_ingreso = ingresos.objects.create(detalle=detalle, monto=monto)
    return redirect('/')

def formGas(request):
    return render (request, 'formGas.html')

def nuevoGasto(request):
    detalle = request.POST.get('gasto-Detalle', False)
    monto = request.POST.get('gasMonto', False)

    nuevo_ingreso = gastos.objects.create(detalle=detalle, monto=monto)
    return redirect('/')