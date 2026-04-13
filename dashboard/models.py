from django.db import models

# Create your models here.
class ingresos(models.Model):
    fecha = models.DateField(auto_now_add=True)
    detalle = models.CharField(max_length=200)
    monto = models.FloatField(default=0)

    def __str__(self):
        return self.detalle

class gastos(models.Model):
    fecha = models.DateField(auto_now_add=True)
    detalle = models.CharField(max_length=200)
    monto = models.FloatField(default=0)

    def __str__(self):
        return self.detalle

class balance(models.Model):
    act = ingresos.objects.values_list('monto', flat=True)
    pas = gastos.objects.values_list('monto', flat=True)

