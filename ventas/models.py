from django.db import models

class Venta(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cédula = models.CharField(max_length=10)
    dirección = models.CharField(max_length=50)
    teléfono = models.CharField(max_length=10)
    correo = models.CharField(max_length=50)
    fecha = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    iva = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    descuento = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre + ' ' + self.apellido