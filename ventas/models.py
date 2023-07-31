from django.db import models

class Cliente(models.Model):
    
        nombre = models.CharField(max_length=50)
        apellido = models.CharField(max_length=50)
        cédula = models.CharField(max_length=10)
        dirección = models.CharField(max_length=50)
        teléfono = models.CharField(max_length=10)
        correo = models.CharField(max_length=50)
        fecha = models.DateField(auto_now=True)
    
        def __str__(self):
            return self.nombre + ' ' + self.apellido
        
class Producto(models.Model):
        
        nombre = models.CharField(max_length=50)
        descripción = models.CharField(max_length=50)
        marca = models.CharField(max_length=50)
        talla = models.CharField(max_length=50)
        color = models.CharField(max_length=50)
        material = models.CharField(max_length=50)
        precio = models.DecimalField(max_digits=10, decimal_places=2)
        stock = models.IntegerField()
        fecha = models.DateField(auto_now=True)
        
        def __str__(self):
            return self.nombre + ' ' + self.marca

class Venta(models.Model):

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    descuento = models.DecimalField(max_digits=10, decimal_places=2)
    iva = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.cliente + ' ' + self.producto + ' ' + self.total